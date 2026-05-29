from flask import Blueprint, request

from app.utils.crud import execute, query_all

requirement_bp = Blueprint('requirement_bp', __name__)

# 定义查询需求列表的接口，路径是/，只允许GET请求
@requirement_bp.route('/', methods=['GET'])
def list_requirements():
    user_name = request.args.get('user_name') # 从请求的参数里，拿到要查询的用户名
    if user_name: # 如果传了用户名，就只查询这个用户自己的需求
        sql = """
        SELECT id, user_name, use_case, duration_days, budget_min, budget_max, seat_count, config_need,
               DATE_FORMAT(created_at, '%%Y-%%m-%%d %%H:%%i:%%s') AS created_at
        FROM user_requirements
        WHERE user_name=%s
        ORDER BY id DESC
        """
        return {'data': query_all(sql, (user_name,))}
    sql = """ 
    SELECT id, user_name, use_case, duration_days, budget_min, budget_max, seat_count, config_need,
           DATE_FORMAT(created_at, '%%Y-%%m-%%d %%H:%%i:%%s') AS created_at
    FROM user_requirements
    ORDER BY id DESC
    """
    return {'data': query_all(sql)}# 如果没传用户名，就查询所有用户的需求，这是给管理员用的


@requirement_bp.route('/', methods=['POST'])# 定义创建用户需求的接口，路径是/，只允许POST请求
def create_requirement():
    body = request.get_json(force=True)# 接收前端发过来的JSON请求体，也就是用户填的用车需求
    sql = """
    INSERT INTO user_requirements (user_name, use_case, duration_days, budget_min, budget_max, seat_count, config_need)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    execute(sql, (
        body.get('user_name'),
        body.get('use_case'),
        body.get('duration_days', 1),
        body.get('budget_min'),
        body.get('budget_max'),
        body.get('seat_count'),
        body.get('config_need')
    ))
    return {'message': 'created'}


@requirement_bp.route('/<int:rid>', methods=['PUT'])# 定义更新用户需求的接口，路径是/<需求ID>，只允许PUT请求
def update_requirement(rid):
    body = request.get_json(force=True)
    sql = """
    UPDATE user_requirements
    SET user_name=%s, use_case=%s, duration_days=%s, budget_min=%s, budget_max=%s, seat_count=%s, config_need=%s
    WHERE id=%s
    """
    execute(sql, (
        body.get('user_name'),
        body.get('use_case'),
        body.get('duration_days', 1),
        body.get('budget_min'),
        body.get('budget_max'),
        body.get('seat_count'),
        body.get('config_need'),
        rid
    ))
    return {'message': 'updated'}
