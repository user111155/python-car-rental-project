from app.utils.db import get_conn# 导入刚才的连接函数，从db.py拿数据库连接


def query_all(sql, params=None):# 通用查询函数：用来执行查询SQL，返回所有结果
    conn = get_conn() # 获取数据库连接
    try:
        with conn.cursor() as cursor:# 创建游标，with语句自动帮我们关闭游标
            cursor.execute(sql, params or ())#  执行SQL，用预处理参数传参，彻底防止SQL注入，  params为空的话传空元组，避免报错
            return cursor.fetchall()# 返回所有查询结果，是字典的列表，每个元素是一行数据
    finally:
        conn.close()


def execute(sql, params=None):#  通用执行函数：用来执行增、删、改的写操作
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            affected = cursor.execute(sql, params or ())
            return affected
    finally:
        conn.close()
