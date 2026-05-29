from flask import Blueprint, request

from app.utils.crud import execute, query_all

rental_bp = Blueprint('rental_bp', __name__)


@rental_bp.route('/cars', methods=['GET'])
def car_list():
    sql = """
    SELECT id, seriesid, seriesname, seriesimg, seriesminprice, seriesmaxprice, average,
           ROUND(seriesminprice / 1000, 2) AS rental_price_day
    FROM car_series
    ORDER BY average DESC, seriesminprice ASC
    """
    return {'data': query_all(sql)}


@rental_bp.route('/payment/preview', methods=['POST'])
def payment_preview():
    body = request.get_json(force=True)
    return {
        'data': {
            'user_id': body.get('user_id'),
            'car_id': body.get('car_id'),
            'car_name': body.get('car_name'),
            'start_date': body.get('start_date'),
            'end_date': body.get('end_date'),
            'total_amount': body.get('total_amount'),
            'pay_status': 'unpaid'
        }
    }


@rental_bp.route('/payment/pay', methods=['POST'])
def payment_pay():
    body = request.get_json(force=True)
    sql = """
    INSERT INTO rental_orders (user_id, car_id, start_date, end_date, status, total_amount)
    VALUES (%s, %s, %s, %s, 'paid', %s)
    """
    execute(sql, (
        body.get('user_id'),
        body.get('car_id'),
        body.get('start_date'),
        body.get('end_date'),
        body.get('total_amount')
    ))
    return {'message': 'paid_success'}


@rental_bp.route('/book', methods=['POST'])
def book_car():
    body = request.get_json(force=True)
    sql = """
    INSERT INTO rental_orders (user_id, car_id, start_date, end_date, status, total_amount)
    VALUES (%s, %s, %s, %s, 'pending', %s)
    """
    execute(sql, (
        body.get('user_id'),
        body.get('car_id'),
        body.get('start_date'),
        body.get('end_date'),
        body.get('total_amount')
    ))
    return {'message': 'booked'}


@rental_bp.route('/orders', methods=['GET'])
def my_orders():
    user_id = request.args.get('user_id')
    params = []
    sql = """
    SELECT ro.id, ro.user_id, ro.car_id,
           DATE_FORMAT(ro.start_date, '%%Y-%%m-%%d') AS start_date,
           DATE_FORMAT(ro.end_date, '%%Y-%%m-%%d') AS end_date,
           ro.status, ro.total_amount,
           ROUND(cs.seriesminprice / 1000, 2) AS rental_price_day,
           cs.seriesname
    FROM rental_orders ro
    LEFT JOIN car_series cs ON ro.car_id=cs.id
    """
    if user_id:
        sql += " WHERE ro.user_id=%s "
        params.append(user_id)# 按ID倒序，最新的订单在前面
    sql += """
    ORDER BY id DESC
    """
    return {'data': query_all(sql, tuple(params))}


@rental_bp.route('/pickup/<int:oid>', methods=['PUT'])
def pickup(oid):
    execute("UPDATE rental_orders SET status='picked_up' WHERE id=%s", (oid,))
    return {'message': 'picked_up'}


@rental_bp.route('/return/<int:oid>', methods=['PUT'])
def return_car(oid):
    execute("UPDATE rental_orders SET status='returned' WHERE id=%s", (oid,))
    return {'message': 'returned'}
