from flask import Blueprint, request

from app.utils.crud import execute, query_all

admin_bp = Blueprint('admin_bp', __name__)

# 定义订单状态统计接口，路径是/orders，只允许GET请求
# 这个接口是统计不同状态的订单数量，给管理员看订单的分布。比如：pending有多少个，paid有多少个，picked_up有多少个，returned有多少个
@admin_bp.route('/orders', methods=['GET'])
def order_manage():
    sql = """
    SELECT status, COUNT(*) AS total
    FROM rental_orders
    GROUP BY status
    """
    return {'data': query_all(sql)}

# 定义库存列表接口，路径是/inventory，只允许GET请求。给管理员看所有车型的库存情况
@admin_bp.route('/inventory', methods=['GET'])
def inventory():
    sql = """
    SELECT seriesname, stock_count, vehicle_status
    FROM car_inventory
    ORDER BY id DESC
    """
    return {'data': query_all(sql)}

# 定义核心运营统计接口，路径是/stats，只允许GET请求，汇总整个系统的运营数据
@admin_bp.route('/stats', methods=['GET'])
def stats():
    order_total = query_all('SELECT COUNT(*) AS value FROM rental_orders')[0]['value']
    car_total = query_all('SELECT COUNT(*) AS value FROM car_series')[0]['value']
    user_total = query_all('SELECT COUNT(*) AS value FROM users')[0]['value']
    return {# 把这三个核心数据返回，给后台首页做数据大屏展示
        'data': {
            'order_total': order_total,
            'car_total': car_total,
            'user_total': user_total
        }
    }

# 定义用户列表接口，路径是/users，只允许GET请求
@admin_bp.route('/users', methods=['GET'])
def user_manage():
    return {'data': query_all("SELECT id, name, phone, username, role FROM users ORDER BY id DESC")}

# 定义创建用户接口，路径是/users，只允许POST请求。管理员可以新增用户
@admin_bp.route('/users', methods=['POST'])
def create_user():
    body = request.get_json(force=True)
    username = (body.get('username') or '').strip()
    if not username:
        return {'message': '用户名不能为空'}, 400
    exists = query_all("SELECT id FROM users WHERE username=%s LIMIT 1", (username,))
    if exists:
        return {'message': '用户名已存在'}, 400

    execute(
        "INSERT INTO users (name, phone, username, password, role) VALUES (%s, %s, %s, %s, %s)",
        (
            body.get('name') or username,
            body.get('phone') or '',
            username,
            body.get('password') or '123456',
            body.get('role') or 'user'
        )
    )
    return {'message': 'created'}

# 定义更新用户接口，路径是/users/<用户ID>，只允许PUT请求。管理员可以修改用户的信息
@admin_bp.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    body = request.get_json(force=True)
    execute(
        "UPDATE users SET name=%s, phone=%s, role=%s WHERE id=%s",
        (
            body.get('name'),
            body.get('phone'),
            body.get('role') or 'user',
            uid
        )
    )
    return {'message': 'updated'}

# 定义删除用户接口，路径是/users/<用户ID>，只允许DELETE请求
@admin_bp.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    execute("DELETE FROM users WHERE id=%s", (uid,))
    return {'message': 'deleted'}

# 定义车型管理接口，路径是/cars，只允许GET请求
# 多表关联：车型表 + 库存表，把车型信息和对应的库存信息一起查出来
@admin_bp.route('/cars', methods=['GET'])
def car_manage():
    sql = """
    SELECT cs.id, cs.seriesid, cs.seriesname, cs.seriesimg, cs.seriesminprice, cs.seriesmaxprice, cs.average,
           ROUND(cs.seriesminprice / 1000, 2) AS rental_price_day,
           IFNULL(ci.stock_count, 0) AS stock_count, IFNULL(ci.vehicle_status, 'available') AS vehicle_status
    FROM car_series cs
    LEFT JOIN car_inventory ci ON cs.seriesname=ci.seriesname
    ORDER BY cs.id DESC
    """
    return {'data': query_all(sql)}

# 定义所有订单列表接口，路径是/orders/all，只允许GET请求
# 三表关联：订单表 + 用户表 + 车型表，把订单、下单用户、车型信息一起查出来
@admin_bp.route('/orders/all', methods=['GET'])
def order_manage_list():
    sql = """
    SELECT ro.id, ro.user_id, u.username, ro.car_id, cs.seriesname,
           DATE_FORMAT(ro.start_date, '%%Y-%%m-%%d') AS start_date,
           DATE_FORMAT(ro.end_date, '%%Y-%%m-%%d') AS end_date,
           ro.status, ro.total_amount
    FROM rental_orders ro
    LEFT JOIN users u ON ro.user_id=u.id
    LEFT JOIN car_series cs ON ro.car_id=cs.id
    ORDER BY ro.id DESC
    """
    return {'data': query_all(sql)}

# 定义更新订单状态接口，路径是/orders/<订单ID>/status，只允许PUT请求
# 管理员可以修改订单的状态
@admin_bp.route('/orders/<int:oid>/status', methods=['PUT'])
def update_order_status(oid):
    body = request.get_json(force=True)
    status = body.get('status')
    execute("UPDATE rental_orders SET status=%s WHERE id=%s", (status, oid))
    return {'message': 'updated'}

# 定义更新车型库存状态接口，路径是/cars/<车型ID>/status，只允许PUT请求
# 管理员可以修改车型的库存数量和车辆状态
@admin_bp.route('/cars/<int:cid>/status', methods=['PUT'])
def update_car_status(cid):
    body = request.get_json(force=True)
    stock_count = body.get('stock_count')
    vehicle_status = body.get('vehicle_status')
    row = query_all("SELECT seriesname FROM car_series WHERE id=%s LIMIT 1", (cid,))
    if not row:
        return {'message': '车型不存在'}, 404
    seriesname = row[0]['seriesname']
    exists = query_all("SELECT id FROM car_inventory WHERE seriesname=%s LIMIT 1", (seriesname,))
    if exists:
        execute(
            "UPDATE car_inventory SET stock_count=%s, vehicle_status=%s WHERE seriesname=%s",
            (stock_count, vehicle_status, seriesname)
        )
    else:
        execute(
            "INSERT INTO car_inventory (seriesname, stock_count, vehicle_status) VALUES (%s, %s, %s)",
            (seriesname, stock_count, vehicle_status)
        )
    return {'message': 'updated'}

# 定义删除车型接口，路径是/cars/<车型ID>，只允许DELETE请求
# 管理员可以删除车型，同时删除对应的库存记录，保证数据一致
@admin_bp.route('/cars/<int:cid>', methods=['DELETE'])
def delete_car(cid):
    row = query_all("SELECT seriesname FROM car_series WHERE id=%s LIMIT 1", (cid,))
    if not row:
        return {'message': '车型不存在'}, 404
    seriesname = row[0]['seriesname']
    execute("DELETE FROM car_series WHERE id=%s", (cid,))
    execute("DELETE FROM car_inventory WHERE seriesname=%s", (seriesname,))
    return {'message': 'deleted'}

# 定义用户需求统计接口，路径是/requirements/stats，只允许GET请求
@admin_bp.route('/requirements/stats', methods=['GET'])
def requirement_stats():
    sql = """
    SELECT use_case, config_need, COUNT(*) AS total, AVG(duration_days) AS avg_duration_days,
           AVG(budget_min) AS avg_budget_min, AVG(budget_max) AS avg_budget_max
    FROM user_requirements
    GROUP BY use_case, config_need
    ORDER BY total DESC
    """
    return {'data': query_all(sql)}
