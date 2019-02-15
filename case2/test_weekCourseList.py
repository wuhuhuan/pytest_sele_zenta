# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:04
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : test_weekCourseList.py
# @Software: PyCharm
"""
case/test_houtai.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
"""
import pytest
import time
from case2.text import Text
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
#u"本周直播课表(2.11~2.15)"
test_text_data = [(loc_text_1,u"本周直播课表(2.11~2.15)"),(loc_text_2, u"周一"),(loc_text_3, u"周二"),(loc_text_4, u"周三"),(loc_text_5, u"周四"),(loc_text_6, u"周五"),(loc_text_7, u"盘前"),(loc_text_8, u"盘中"),(loc_text_9, u"盘后"),(loc_text_10, u"9:30"),(loc_text_11, u"15:00")]

ids=[i[1] for i in test_text_data]
class Testweekcourselist:
    @pytest.mark.test_clickAll_liveList
    @pytest.mark.parametrize("loc_helpwe_x, text", test_text_data, ids=[i[1] for i in test_text_data])
    def test_clickAll_liveList(self,weekCourseList,loc_helpwe_x,text):
        '''看直播页-点击全部筛选按钮'''
        result=weekCourseList.get_text1(loc_helpwe_x)
        assert result==text

    @pytest.mark.getnum
    def test_getWeekCourseListNum(self,weekCourseList):
        weekCourseList.addEles(weekCourseList.beforeDishs, "/html/body/div/div[2]/div[3]/div[", "]/a/div[1]", weekCourseList.feeEles,weekCourseList.chargedEles)
        time.sleep(2)




if __name__=="__main__":
    pytest.main(["-s", "-v","-m","getnum","--browser=chrome","--host=https://m.dev.hbec.com", "test_weekCourseList.py","--html=./report/report.html","--self-contained-html"])
    #pytest.main(["-s", "-v","--browser=chrome","--host=https://m.dev.hbec.com", "test_weekCourseList.py","--html=./report/report.html","--self-contained-html"])
