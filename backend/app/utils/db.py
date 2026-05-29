import pymysql# 导入pymysql：Python操作MySQL的官方驱动，负责和MySQL服务通信

from app.config import Config# 导入配置类：从全局配置文件读取数据库的地址、账号等配置，所有模块统一从这里读


def get_conn(): # 创建MySQL连接
    return pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        charset=Config.DB_CHARSET,
        cursorclass=pymysql.cursors.DictCursor, # 关键配置：游标用DictCursor，查询结果的每一行都是字典格式：{字段名: 字段值}
        autocommit=True# 自动提交事务，不用业务代码手动commit
    )
