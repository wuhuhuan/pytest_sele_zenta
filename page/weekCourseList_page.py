# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 15:38
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : weekCourseList_page.py
# @Software: PyCharm
from common.base import Base
from common.TESTDB import sqled
import time
from selenium import webdriver

class WeekCourseList(Base):
    # 栏目文案定位

    def __init__(self,driver):
        self.timeout = 10
        self.t = 0.5
        self.driver = driver
    def get_text1(self,loc):
        text=self.findElement(loc).text
        return text
