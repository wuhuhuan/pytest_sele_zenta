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



    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginfindPortfolioRecordButton1
    def test_openedAccountLoginfindPortfolioRecordButton1(self):
        """已开户已登录点击目标付费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(4)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginfindPortfolioRecordButton2
    def test_openedAccountLoginfindPortfolioRecordButton2(self):
        """已开户已登录点击普通收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(4)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginfindPortfolioRecordButton3
    def test_openedAccountLoginfindPortfolioRecordButton3(self):
        """已开户已登录点击免费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginclickviewpointFeeRecord
    def test_openedAccountLoginclickviewpointFeeRecord(self):
        """已登陆点击免费文章记录"""
        self.index.clickviewpointRecord('0')
        result1 = self.index.is_clickviewpointRecordAdviserName_success()
        result2 = self.index.is_clickviewpointRecordAdviserPicture_success()
        result3 = self.index.is_both_true(result1, result2)
        print("result的结果为%s" % result1, result2)
        assert result3

    @pytest.mark.openedAccountLoginclickviewpointChargedRecord
    def test_openedAccountLoginclickviewpointChargedRecord(self):
        """已登陆点击付费文章记录"""
        self.index.clickviewpointRecord('1')
        result = self.index.is_clickviewpointRecord_success()
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.openedAccountLoginclickvideoDetailFeeRecord
    def test_openedAccountLoginclickvideoDetailFeeRecord(self):
        """已登陆点击免费视频文章记录"""
        self.index.clickvideoDetailRecord("0")
        result = self.index.is_clickvideoDetailRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginclickvideoDetailChargedRecord
    def test_openedAccountLoginclickvideoDetailChargedRecord(self):
        """已登陆点击付费视频文章记录"""
        self.index.clickvideoDetailRecord("1")
        result = self.index.is_clickvideoDetailRecord_success("1")
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.clicktwLiveFeeLoginRecord
    def test_clicktwLiveFeeLoginRecord(self):
        """已登陆点击免费图文直播记录"""
        self.index.clicktwLiveRecord("0")
        result = self.index.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clicktwLiveChargedLoginRecord
    def test_clicktwLiveChargedLoginRecord(self):
        """已登陆点击付费图文直播记录"""
        self.index.clicktwLiveRecord("1")
        result = self.index.is_clicktwLiveRecord_success("1")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginclickliveFeeVideRecord
    def test_openedAccountLoginclickliveFeeVideRecord(self):
        """已登录点击免费视频直播记录"""
        self.index.clickliveVideoRecord("0")
        result = self.index.is_clickliveVideoRecord_success("0")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.openedAccountLoginclickliveChargedVideRecord
    def test_openedAccountLoginclickliveChargedVideRecord(self):
        """已登录点击付费视频直播记录"""
        self.index.clickliveVideoRecord("1")
        result = self.index.is_clickliveVideoRecord_success("1")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.openedAccountLoginclickcourseFeeRecord
    def test_openedAccountLoginclickcourseFeeRecord(self):
        """已登录点击免费课程"""
        self.index.clickcourse('0')
        result = self.index.is_clickcourse_success('0')
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.openedAccountLoginclickcourseChargedRecord
    def test_openedAccountLoginclickcourseChargeRecord(self):
        """已登录点击付费课程"""
        # self.index.getCourseNums()
        self.index.clickcourse('1')
        result = self.index.is_clickcourse_success('1')
        print("result的结果为%s" % result)
        assert result


if __name__ == "__main__":
    #pytest.main(["-s", "-v","-m=openedAccountLoginclickliveFeeVideRecord","--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_openedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
    pytest.main(["-s", "-v", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_openedAccountLogin.py", "--html=./report.html","--self-contained-html"])

    #pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
