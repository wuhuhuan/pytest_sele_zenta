# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:04
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : test_weekCourseList.py
# @Software: PyCharm
import pytest
from case2.text import Text
from page.weekCourseList_page import WeekCourseList
url_weekCourseList="/adviser/index/weekCourseList.htm"
# 栏目文案测试数据
loc_text_1 = ("xpath", "/html/body/div/div[1]")
loc_text_2 = ("xpath", "/html/body/div/div[2]/div[1]/div[1]")
loc_text_3 = ("xpath", "/html/body/div/div[2]/div[1]/div[2]")
loc_text_4 = ("xpath", "/html/body/div/div[2]/div[1]/div[3]")
loc_text_5 = ("xpath", "/html/body/div/div[2]/div[1]/div[4]")
loc_text_6 = ("xpath", "/html/body/div/div[2]/div[1]/div[5]")
loc_text_7 = ("xpath", "/html/body/div/div[2]/div[2]/span")
loc_text_8 = ("xpath", "/html/body/div/div[2]/div[4]/span")
loc_text_9 = ("xpath", "/html/body/div/div[2]/div[6]/span")
loc_text_10 = ("xpath", "/html/body/div/div[2]/div[2]/i")
loc_text_11 = ("xpath", "/html/body/div/div[2]/div[6]/i")
aa = Text()
param= aa.getCourseText()
test_text_data = [(loc_text_1, param),
            (loc_text_2, u"周一"),
            (loc_text_3, u"周二"),
            (loc_text_4, u"周三"),
            (loc_text_5, u"周四"),
            (loc_text_6, u"周五"),
            (loc_text_7, u"盘前"),
            (loc_text_8, u"盘中"),
            (loc_text_9, u"盘后"),
            (loc_text_10, u"9:30"),
            (loc_text_11, u"15:00")]

"""
case/test_add_bug.py
** 吴沪欢
"""

class TestWeekCourseList():
    @pytest.fixture(autouse=True)
    def maximize(self, driver, host):
        '''初始化'''
        self.weekcourseList = WeekCourseList(driver)
        driver.maximize_window()
        driver.get(host + url_weekCourseList)

    @pytest.mark.parametrize("loc_courselist_x, text", test_text_data, ids=[i[1] for i in test_text_data])
    def test_text(self,loc_courselist_x, text):
        '''页面元素显示'''
        t1 = self.weekcourseList.get_text1(loc_courselist_x)
        assert t1 == text
if __name__ == "__main__":
    #pytest.main(["-s", "-v","-m=test_text","--browser=chrome","--host=https://m.dev.hbec.com", "test_weekCourseList.py","--html=./report/report.html","--self-contained-html"])
    pytest.main(["-s", "-v", "--browser=chrome","--host=https://m.dev.hbec.com", "test_weekCourseList.py", "--html=./report/report.html","--self-contained-html"])
