# -*- coding: UTF-8 -*-
# 建立数据库连接
import pymysql
class sqled:

    def __init__(self,host='10.0.30.59', user = "adviser", passwd="123123", db="iadb", port=3306, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.Connect(host=self.host,user=self.user,passwd=self.passwd ,db=self.db ,port=self.port,charset=self.charset)

    def sql(self,sql="SELECT adviserid FROM tg_adviserinfo"):
        # 获取游标
        self.cursor = self.conn.cursor()
        # print(conn)
        # print(cursor)

        # 1、从数据库中查询
        # sql="INSERT INTO login(user_name,pass_word)"
        # cursor执行sql语句
        self.cursor.execute(sql)
        # 打印执行结果的条数
        #print(self.cursor.fetchone())
        aa=[]
        try:
            # 获取所有记录列表
            results = self.cursor.fetchall()
            for row in results:
                fname = row[0]
                aa.append(row[0])
                # 打印结果
                print "fname=%s" % fname
        except:
            print "Error: unable to fecth data"
        return aa
    def close(self):
        self.conn.close()
        self.cursor.close()
if __name__=='__main__':
    sqle=sqled('10.0.30.59',  "adviser", "123123", "iadb", 3306, "utf8")
    aaa =sqle.sql("select comment from tg_live_menu   order by live_islive asc,live_endtime desc,live_starttime asc")
    print("--------------")
    print("aaa--------------:%s"%type(aaa))
    print len(aaa)


