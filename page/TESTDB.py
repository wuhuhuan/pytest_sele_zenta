# -*- coding: UTF-8 -*-
# 建立数据库连接
import pymysql
conn = pymysql.Connect(
    host='10.0.30.59',##mysql服务器地址
    port=3306,##mysql服务器端口号
    user='adviser',##用户名
    passwd='123123',##密码
    db='iadb',##数据库名
    charset='utf8'##连接编码
)

# 获取游标
cursor = conn.cursor()
# print(conn)
# print(cursor)

# 1、从数据库中查询
# sql="INSERT INTO login(user_name,pass_word)"
sql = "SELECT adviserid FROM tg_adviserinfo"
# cursor执行sql语句
cursor.execute(sql)
# 打印执行结果的条数
print(cursor.fetchone())

conn.close()
cursor.close()
