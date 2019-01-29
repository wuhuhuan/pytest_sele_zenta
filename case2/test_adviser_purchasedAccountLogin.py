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
class TestClick():


    @pytest.fixture(autouse=True)
    def maximize(self,driver,host):
        '''初始化'''
        self.index = adviserMain(driver)
        self.index.getPortfolioNums
        driver.maximize_window()
        driver.get(host + url_hou)

    @pytest.mark.usefixtures("purchasedAccountLogin")
    @pytest.mark.findPortfolioRecordpurchasedButton1
    def test_findPortfolioRecordpurchasedButton1(self):
        """已购买点击目标付费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.findPortfoliopurchasedRecordButton2
    def test_findPortfoliopurchasedRecordButton2(self):
        """已购买点击普通收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result




    @pytest.mark.purchasedAccountLoginclickviewpointChargedRecord
    def test_purchasedAccountLoginclickviewpointChargedRecord(self):
        """已购买点击付费文章记录"""
        self.index.clickviewpointRecord('1')
        result = self.index.is_clickviewpointRecord_Reverse()
        print("result的结果为%s" % result)
        assert result




    @pytest.mark.purchasedAccountLoginclickvideoDetailChargedRecord
    def test_purchasedAccountLoginclickvideoDetailChargedRecord(self):
        """已购买点击付费视频文章记录"""
        self.index.clickvideoDetailRecord("1")
        result = self.index.is_clickvideoDetailRecord_success("0")
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.purchasedAccountLoginclicktwLiveFeeRecord
    def test_purchasedAccountLoginclicktwLiveFeeRecord(self):
        """已购买点击免费图文直播记录"""
        self.index.clicktwLiveRecord("0")
        result = self.index.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.purchasedAccountLoginclicktwLiveChargedRecord
    def test_purchasedAccountLoginclicktwLiveChargedRecord(self):
        """已购买点击付费图文直播记录"""
        self.index.clicktwLiveRecord("1")
        result = self.index.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result






    @pytest.mark.purchasedAccountLoginclickliveChargedVideoRecord
    def test_purchasedAccountLoginclickliveChargedVideoRecord(self):
        """已购买登录点击付费视频直播记录"""
        self.index.clickliveVideoRecord("1")
        result = self.index.is_clickliveVideopurchasedRecord_success()
        print("result的结果为%s" % result)
        assert result




    @pytest.mark.purchasedAccountLoginclickcourseFeeRecord
    def test_purchasedAccountLoginclickcourseFeeRecord(self):
        """已购买点击免费课程"""
        self.index.clickcourse('0')
        result = self.index.is_clickcourse_success('0')
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.purchasedAccountLoginclickcourseChargedRecord
    def test_purchasedAccountLoginclickcourseChargedRecord(self):
        """已购买点击付费课程"""
        self.index.clickcourse('1')
        result = self.index.is_clickcourse_success('0')
        print("result的结果为%s" % result)
        assert result


if __name__ == "__main__":
    #pytest.main(["-s", "-v","-m=openedAccountLoginclickliveVideoFeeRecord","--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
    pytest.main(["-s", "-v", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py", "--html=./report/report.html","--self-contained-html"])

    #pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
