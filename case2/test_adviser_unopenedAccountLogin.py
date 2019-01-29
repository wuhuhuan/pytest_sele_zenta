#-*- coding: utf-8 -*-
import pytest
import time
from page.adviserMain import adviserMain
url_hou ="/adviser/index/main"

url_hou1 =""
"""
case/test_add_bug.py
** 吴沪欢
"""

# 栏目文案定位
loc_menuid_1 = ("xpath", "/html/body/div[1]/div[2]/div/div[3]/span[2]")
loc_menuid_2 = ("xpath", "/html/body/div[1]/div[2]/div/div[5]/span[2]")
loc_menuid_3 = ("xpath", "/html/body/div[1]/div[2]/div/div[7]/span[2]")
loc_menuid_4 = ("xpath", "/html/body/div[1]/div[2]/div/div[9]/span[2]")

# 栏目文案测试数据
test_menuid_data = [
    (loc_menuid_1, u"选股择时，省时省心"),
    (loc_menuid_2, u"每日文章，洞悉市场"),
    (loc_menuid_3, u"直面投顾，即时交流"),
    (loc_menuid_4, u"系统学习，进阶投资")
]
class TestClick():


    @pytest.fixture(autouse=True)
    def maximize(self,driver,host):
        '''初始化'''
        self.index = adviserMain(driver)
        self.index.getPortfolioNums
        driver.maximize_window()
        driver.get(host + url_hou)


    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton1
    def test_unopenedAccountLoginfindPortfolioRecordButton1(self):
        """未开户已登录点击目标收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton2
    def test_unopenedAccountLoginfindPortfolioRecordButton2(self):
        """未开户已登录点击普通收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton3
    def test_unopenedAccountLoginfindPortfolioRecordButton3(self):
        """未开户已登录点击未收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(3)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.unopenedAccountLoginclickvideoDetailFeeRecord
    def test_unopenedAccountLoginclickvideoDetailFeeRecord(self):
        """未开户点击免费视频文章记录"""
        self.index.clickvideoDetailRecord("0")
        result = self.index.is_clickvideoDetailRecord_success("0")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.unopenedAccountLoginclickvideoDetailChargedRecord
    def test_unopenedAccountLoginclickvideoDetailChargedRecord(self):
        """未开户点击付费视频文章记录"""
        self.index.clickvideoDetailRecord("1")
        result = self.index.is_clickvideoDetailRecord_success("1")
        print("result的结果为%s" % result)
        assert result




    @pytest.mark.unopenedAccountLoginclickcourseFeeRecord
    def test_unopenedAccountLoginclickcourseFeeRecord(self):
        """未开户点击免费课程"""
        self.index.clickcourse('0')
        result = self.index.is_clickcourse_success('0')
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.unopenedAccountLoginclickcourseChargedRecord
    def test_unopenedAccountLoginclickcourseChargedRecord(self):
        """未开户点击付费课程"""
        # self.index.getCourseNums()
        self.index.clickcourse('1')
        result = self.index.is_clickcourse_success('1')
        print("result的结果为%s" % result)
        assert result


if __name__ == "__main__":
    #pytest.main(["-s", "-v","-m=openedAccountLoginclickliveVideoFeeRecord","--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
    pytest.main(["-s", "-v", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py", "--html=./report/report.html","--self-contained-html"])

    #pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
