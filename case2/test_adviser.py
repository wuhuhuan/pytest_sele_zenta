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


    @pytest.fixture(scope="module")
    def maximize(self,driver):
        '''初始化'''
        self.index = adviserMain(driver)
        self.index.getPortfolioNums
        driver.maximize_window()

    @pytest.fixture(autouse=True)
    def open_houtai(self, driver, host):
        '''回到主页'''
        driver.get(host + url_hou)
    @pytest.mark.clickFindAdviserButton
    def test_clickFindAdviserButton(self):
        """点击找投顾按钮"""
        self.index.clickFindAdviserButton()
        result = self.index.is_clickFindAdviserButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_clickliveButton(self):
        """点击观看按钮"""
        self.index.clickliveButton()
        result = self.index.is_clickliveButton_sucess()
        print("result的结果为%s" % result)
        assert result
    def test_clickfindPortfolioButton(self):
        """点击模拟盘按钮"""
        self.index.clickfindPortfolioButton()
        time.sleep(3)
        result = self.index.is_clickfindPortfolioButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_ViewpointListButton(self):
        """点击观点按钮"""
        self.index.clickViewpointListButton()
        result = self.index.is_clickViewpointListButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_CourseButton(self):
        """点击课程按钮"""
        self.index.clickCourseButton()
        result = self.index.is_clickCourseButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_QuestionButton(self):
        """点击问个股按钮"""
        self.index.clickQuestionButton()
        result = self.index.is_clickQuestionButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_findPortfolioMoreButton(self):
        """点击模拟盘更多按钮"""
        self.index.clickfindPortfolioMoreButton()
        result = self.index.is_clickfindPortfolioMoreButton_success()
        print("result的结果为%s" % result)
        assert result

    def test_liveMoreButton(self):
        """点击直播更多按钮"""
        self.index.clickliveMoreButton()
        time.sleep(2)
        result = self.index.is_clickliveMoreButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_ViewpointListMoreButton(self):
        """点击知观点更多按钮"""
        self.index.clickViewpointListMoreButton()
        result = self.index.is_clickViewpointListMoreButton_sucess()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.CourseMoreButton
    def test_CourseMoreButton(self):
        """点击课程更多按钮"""
        self.index.clickCourseMoreButton()
        result = self.index.is_clickCourseMoreButton_success()
        print("result的结果为%s" % result)
        assert result

    def test_eliteAdviserMoreButton(self):
        """点击精英投顾更多按钮"""
        self.index.clickeliteAdviserMoreButton()
        result = self.index.is_clickeliteAdviserMoreButton_success()
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.findPortfolioRecordButton1
    def test_findPortfolioRecordButton1(self):
        """未登陆点击目标付费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(1)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.findPortfolioRecordButton2
    def test_findPortfolioRecordButton2(self):
        """未登陆点击普通付费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(1)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.findPortfolioRecordButton3
    def test_findPortfolioRecordButton3(self):
        """未登陆点击免费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(3)
        result = self.index.is_clickfindPortfolioRecordButton_success(1)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton1
    def test_unopenedAccountLoginfindPortfolioRecordButton1(self):
        """未开户已登录点击目标收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton2
    def test_unopenedAccountLoginfindPortfolioRecordButton2(self):
        """未开户已登录点击普通收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginfindPortfolioRecordButton3
    def test_unopenedAccountLoginfindPortfolioRecordButton3(self):
        """未开户已登录点击未收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(3)
        result = self.index.is_clickfindPortfolioRecordButton_success(2)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginfindPortfolioRecordButton1
    def test_openedAccountLoginfindPortfolioRecordButton1(self):
        """已开户已登录点击目标付费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(1)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginfindPortfolioRecordButton2
    def test_openedAccountLoginfindPortfolioRecordButton2(self):
        """已开户已登录点击普通收费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginfindPortfolioRecordButton3
    def test_openedAccountLoginfindPortfolioRecordButton3(self):
        """已开户已登录点击免费模拟盘记录"""
        self.index.clickfindPortfolioRecordButton(2)
        result = self.index.is_clickfindPortfolioRecordButton_success(3)
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.findPortfolioRecordAdviserButton
    def test_findPortfolioRecordAdviserButton(self):
        """未登陆点击模拟盘投顾信息"""
        self.index.clickfindPortfolioRecordAdviserButton()
        result1 = self.index.is_clickfindPortfoliotaIndexAdviserName_success()
        time.sleep(3)
        result2 = self.index.is_clickfindPortfoliotaIndexAdviserPicture_success()
        result3=self.index.is_both_true(result1,result2)
        print("result的结果为%s" % result1,result2)
        assert result3

    @pytest.mark.clickviewpointRecord
    def test_clickviewpointRecord(self):
        """未登陆点击文章记录"""
        self.index.clickviewpointRecord()
        result1 = self.index.is_clickviewpointRecordAdviserName_success()
        result2 = self.index.is_clickviewpointRecordAdviserPicture_success()
        result3 = self.index.is_both_true(result1, result2)
        print("result的结果为%s" % result1, result2)
        assert result3

    @pytest.mark.clickvideoDetailRecord
    def test_clickvideoDetailRecord(self):
        """未登陆点击视频文章记录"""
        self.index.clickvideoDetailRecord()
        result= self.index.is_clickvideoDetailRecord_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clicktwLiveRecord
    def test_clicktwLiveRecord(self):
        """未登陆点击图文直播记录"""
        self.index.clicktwLiveRecord()
        result= self.index.is_clicktwLiveRecord_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clickliveVideoRecord
    def test_clickliveVideoRecord(self):
        """未登陆点击视频直播记录"""
        self.index.clickliveVideoRecord()
        result = self.index.is_clickliveVideoRecord_success()
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.clickcourseFeeRecord
    def test_clickcourseFeeRecord(self):
        """点击免费课程"""
        self.index.clickcourseFee()
        result = self.index.is_clickcourseFee_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("login")
    @pytest.mark.clickeliteAdviserRecord
    def test_clickeliteAdviserRecord(self):
        """未登陆精英投顾记录"""
        self.index.clickeliteAdviserRecord()
        result1 = self.index.is_clickeliteAdviserRecordAdviserPicture_success()
        result2 = self.index.is_clickeliteAdviserRecordAdviserName_success()
        result3 = self.index.is_both_true(result1, result2)
        print("result的结果为%s" % result1, result2)
        assert result3


    @pytest.mark.checkMenuid
    @pytest.mark.parametrize("loc_adviser, text", test_menuid_data, ids=[i[1] for i in test_menuid_data])
    def test_checkMenuid(self,loc_adviser, text):
        """首页文案验证"""
        t2 = self.index.get_text(loc_adviser)
        assert t2 == text
    @pytest.mark.testa
    def test_aaa(self):
        """aa"""
        eles=self.index.findElements(("xpath", "//div[contains(@class, 'stock-item')]"))
        nums = []
        i=0
        for ele in eles:
            text = str(ele.get_attribute("class"))
            print("属性值为：%s" % text)
            i=i+1
            if text=='stock-item com_tips_aim':
                print("stock-item com_tips_aim:%s" %text)
            elif text=='stock-item com_tips':
                print("stock-item com_tips:%s" % text)
            else:
                print("stock-item:%s" % text)
        time.sleep(3)

    @pytest.mark.baidu
    def test_search(self):
        """aa"""
        self.index.baidu("aaaaaaaaaaa")
        time.sleep(9)
    @pytest.mark.aaaabbbbb
    def test_search1(self):
        """aa"""
        self.index.getPortfolioNums()
        print("jajajjaja")
        
        time.sleep(2)

if __name__ == "__main__":
    pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com","-m","aaaabbbbb", "test_adviser.py","--html=./report/report.html","--self-contained-html"])
    #pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser.py","--html=./report/report.html","--self-contained-html"])
