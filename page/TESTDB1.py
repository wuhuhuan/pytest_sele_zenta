# -*- coding: UTF-8 -*-
# 建立数据库连接
import pymysql
import pymysql
conn = pymysql.connect(host='10.0.30.59', user = "adviser", passwd="123123", db="iadb", port=3306, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT adviserid FROM tg_adviserinfo")
# 打印执行结果的条数
print(cur.fetchone())

