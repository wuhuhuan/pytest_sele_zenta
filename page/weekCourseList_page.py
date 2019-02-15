# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 15:38
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : weekCourseList_page.py
# @Software: PyCharm
from common.base import Base
from common.TESTDB import sqled
from common.TESTDB import sqled
import time
from selenium import webdriver

class WeekCourseList(Base):
    # 课表定位
    loc_1=("xpath","//div[@class='liveSchd-item']")
    beforeDishs=[]
    Intradays=[]
    afterHoursTradings=[]
    feeEles=[]
    chargedEles=[]

    def __init__(self,driver):
        self.timeout = 10
        self.t = 0.5
        self.driver = driver
        self.setLiveEle()
    def get_text1(self,loc):
        text=self.findElement(loc).text
        return text
    def getWeekCourseListNum(self):
        for i in range(1, 6):
            loc_2=("xpath","/html/body/div/div[2]/div[3]/div["+str(i)+"]/a")
            loc_3=("xpath","/html/body/div/div[2]/div[5]/div["+str(i)+"]/a")
            loc_4 = ("xpath", "/html/body/div/div[2]/div[7]/div[" + str(i) + "]/a")
            if self.findElementboolean(loc_2):
                print("beforeDish i:%s" %i)
                self.beforeDishs.append(i)
            elif self.findElementboolean(loc_3):
                print("Intraday i:%s" % i)
                self.Intradays.append(i)
            elif self.findElementboolean(loc_4):
                print("afterHoursTrading i:%s" % i)
                self.afterHoursTradings.append(i)
            else:
                print("没有找到i为:%s" % i)

    # 获取免费、付费 视频定位方法
    def addEles(self,list1=[],beforeloc='',afterloc='',feelist=[],chargedlist=[]):
        cc = sqled()
        for num in list1:
            loc_1=("xpath",str(beforeloc)+str(num)+str(afterloc))
            ele=self.findElement(loc_1)
            Text=self.get_text(loc_1)
            sql="select ischarge from tg_live_menu where comment like "+Text+"%"
            num=cc.sql(sql)
            print("num:%s"%num)
            if num==0:
                feelist.append(ele)
            elif num==1:
                chargedlist.append(ele)
            else:
                print("bibibaocuo")
    def setLiveEle(self):
        self.addEles(self.beforeDishs, "/html/body/div/div[2]/div[3]/div[", "]/a/div[1]", self.feeEles,self.chargedEles)
        self.addEles(self.Intradays, "/html/body/div/div[2]/div[5]/div[", "]/a/div[1]", self.feeEles, self.chargedEles)
        self.addEles(self.afterHoursTradings, "/html/body/div/div[2]/div[7]/div[", "]/a/div[1]", self.feeEles,self.chargedEles)

    def getRecordEle(self,sign):
        try:
            if sign==0:
                return self.feeEles[0]
            elif sign==1:
                return self.chargedEles[0]
            else:
                print("sign值输入有误，字典：0:免费直播、1:收费直播")
        except IndexError:
            if sign==0:
                return self.feeEles[0]
            elif sign==1:
                return self.chargedEles[0]
            else:
                print("sign值输入有误，字典：0:免费直播、1:收费直播")
    def clickFeeRecord(self):
        self.getRecordEle(0).click()
    def clickChargedRecord(self):
        self.getRecordEle(1).click()

# if __name__=="__main__":
#