from flask import Flask
from flask_cors import CORS#导入跨域处理类，让前端（运行在 8080 端口）可以调用后端（运行在 5000 端口）的接口
# 3. 导入所有业务模块的接口蓝图
from app.routes.user_requirements import requirement_bp# 需求管理的接口
from app.routes.data_manage import data_bp
from app.routes.recommend import recommend_bp
from app.routes.rental_service import rental_bp
from app.routes.admin import admin_bp
from app.routes.auth import auth_bp
from app.utils.crud import execute# 导入通用的SQL执行工具，用来做数据库迁移


def _safe_migrate():# 定义安全的数据库迁移函数：项目升级时自动更新旧表的结构，不用手动改数据库
    alter_sql = [
        "ALTER TABLE users ADD COLUMN username VARCHAR(50) NULL",
        "ALTER TABLE users ADD COLUMN password VARCHAR(100) NULL",
        "ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'user'",
        "UPDATE users SET username=name WHERE username IS NULL",
        "UPDATE users SET password='123456' WHERE password IS NULL",
        "UPDATE users SET role='user' WHERE role IS NULL",
        "ALTER TABLE user_requirements ADD COLUMN duration_days INT DEFAULT 1",
        "ALTER TABLE user_requirements ADD COLUMN config_need VARCHAR(100) NULL"
    ]
    for sql in alter_sql:
        try:
            execute(sql)
        except Exception:
            # Ignore duplicate-column and compatibility issues in incremental runs.
            pass


def create_app():    # 定义应用工厂函数
    app = Flask(__name__, static_folder='../static', static_url_path='/static')    # 创建Flask应用，配置静态文件路径，用来放前端的静态资源
    CORS(app)    # 开启跨域支持，让前端可以正常调用后端接口
    _safe_migrate()    # 应用启动时自动执行数据库迁移，更新表结构
#  把所有业务模块的蓝图，注册到应用上，给它们加统一的/api前缀。业务接口，都挂载到这个Web应用上，前端才能访问到
    app.register_blueprint(requirement_bp, url_prefix='/api/requirements')
    app.register_blueprint(data_bp, url_prefix='/api/data')
    app.register_blueprint(recommend_bp, url_prefix='/api/recommend')
    app.register_blueprint(rental_bp, url_prefix='/api/rental')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    @app.route('/api/health', methods=['GET'])     #  注册健康检查接口，用来检查服务是否正常运行
    def health():
        return {'message': 'ok'}

    return app
