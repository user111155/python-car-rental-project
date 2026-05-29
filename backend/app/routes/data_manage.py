from flask import Blueprint

from app.utils.crud import query_all

data_bp = Blueprint('data_bp', __name__)


@data_bp.route('/users', methods=['GET'])
def users():
    return {'data': query_all('SELECT id, name, phone FROM users ORDER BY id DESC')}


@data_bp.route('/cars', methods=['GET'])
def cars():
    sql = """
    SELECT id, seriesid, seriesname, seriesimg, seriesminprice, seriesmaxprice, average, specids, create_time
    FROM car_series
    ORDER BY id DESC
    """
    return {'data': query_all(sql)}


@data_bp.route('/orders', methods=['GET'])
def orders():
    sql = """
    SELECT id, user_id, car_id, start_date, end_date, status, total_amount
    FROM rental_orders
    ORDER BY id DESC
    """
    return {'data': query_all(sql)}
