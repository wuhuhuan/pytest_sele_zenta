# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 8:42
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : text.py
# @Software: PyCharm
from jpype import *
import os.path
class Text:
    def getCourseText(self):
        jarpath=os.path.join(os.path.abspath('.'),'D:/')
        startJVM("D:/Program Files (x86)/Java/jdk1.7.0_79/jre/bin/client/jvm.dll","-ea","-Djava.class.path=%s"%(jarpath+'TestDay.jar'))
        JDClass = JClass("com.wuhuhuan.JodaDateUtils")
        jd = JDClass
        #jd = JPackage("com.wuhuhuan").JodaDateUtils() #两种创建jd的方法
        jprint = java.lang.System.out.println
        param=jd.getText()
        jprint(jd.getText())
        # shutdownJVM()
        return param