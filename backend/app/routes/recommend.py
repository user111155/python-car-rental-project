from flask import Blueprint, request

from app.services.recommend_service import build_recommend_list
# 创建推荐模块的蓝图，把所有和推荐相关的接口打包在一起
# 后面 __init__.py 会把这个蓝图注册到Flask应用里，这样前端就能访问到这个接口了
recommend_bp = Blueprint('recommend_bp', __name__)


@recommend_bp.route('/', methods=['POST'])
def recommend():
    body = request.get_json(force=True)# 接收前端发过来的JSON请求体，也就是用户填的所有用车需求
    result = build_recommend_list(
        budget_min=body.get('budget_min'),
        budget_max=body.get('budget_max'),
        seat_count=body.get('seat_count'),
        use_case=body.get('use_case', ''),
        config_need=body.get('config_need', ''),
        order_by=body.get('order_by', 'match_score')
    )
    return {'data': result}
