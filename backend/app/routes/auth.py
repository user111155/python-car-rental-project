from flask import Blueprint, request# 1. 导入Flask的Blueprint，用来创建路由蓝图（把一组相关的接口打包）。导入request（里面有数据），用来接收前端发过来的请求数据

from app.utils.crud import execute, query_all

auth_bp = Blueprint('auth_bp', __name__)# 创建认证模块的蓝图，把所有和登录注册相关的接口，都打包到这个蓝图里

# 定义注册接口，路径是/register，只允许POST请求（数据敏感或者多 用post，无长度限制）
@auth_bp.route('/register', methods=['POST'])
def register():
    body = request.get_json(force=True)# 接收前端发过来的JSON请求体，拿到用户填的注册信息，无论什么信息，强行把它当成 JSON 
    username = (body.get('username') or '').strip()#不要空格空行
    password = (body.get('password') or '').strip()
    phone = (body.get('phone') or '').strip()

    if not username or not password:
        return {'message': '用户名和密码不能为空'}, 400

    exists = query_all('SELECT id FROM users WHERE username=%s LIMIT 1', (username,))
    if exists:
        return {'message': '用户名已存在'}, 400

    execute(
        'INSERT INTO users (name, phone, username, password, role) VALUES (%s, %s, %s, %s, %s)',
        (username, phone, username, password, 'user')
    )
    return {'message': '注册成功'}

# 定义登录接口，路径是/login，只允许POST请求
@auth_bp.route('/login', methods=['POST'])
def login():
    body = request.get_json(force=True)
    username = (body.get('username') or '').strip()
    password = (body.get('password') or '').strip()

    sql = """
    SELECT id, name, phone, username, role
    FROM users
    WHERE username=%s AND password=%s
    LIMIT 1
    """
    users = query_all(sql, (username, password))
    if not users:
        return {'message': '账号或密码错误'}, 400

    return {'message': '登录成功', 'data': users[0]}
