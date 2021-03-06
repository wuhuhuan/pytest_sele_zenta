#-*- coding: utf-8 -*-
import pytest
import time

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
    @pytest.mark.clickFindAdviserButton
    def test_clickFindAdviserButton(self,index):
        """点击找投顾按钮"""
        index.clickFindAdviserButton()
        result = index.is_clickFindAdviserButton_sucess()
        print("result的结果为%s" % result)
        assert result

    def test_clickliveButton(self,index):
        """点击看直播按钮"""
        index.clickliveButton()
        result = self.index.is_clickliveButton_sucess()
        print("result的结果为%s" % result)
        assert result
    def test_clickfindPortfolioButton(self):
        """点击跟操作按钮"""
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

    @pytest.mark.clickviewpointFeeRecord
    def test_clickviewpointFeeRecord(self):
        """未登陆点击免费文章记录"""
        self.index.clickviewpointRecord('0')
        result1 = self.index.is_clickviewpointRecordAdviserName_success()
        result2 = self.index.is_clickviewpointRecordAdviserPicture_success()
        result3 = self.index.is_both_true(result1, result2)
        print("result的结果为%s" % result1, result2)
        assert result3

    @pytest.mark.clickviewpointChargedRecord
    def test_clickviewpointChargedRecord(self):
        """未登陆点击付费文章记录"""
        self.index.clickviewpointRecord('1')
        result = self.index.is_clickviewpointRecord_success()
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.clickvideoDetailFeeRecord
    def test_clickvideoDetailFeeRecord(self):
        """未登陆点击免费视频文章记录"""
        self.index.clickvideoDetailRecord("0")
        result= self.index.is_clickvideoDetailRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clickvideoDetailChargedRecord
    def test_clickvideoDetailChargedRecord(self):
        """未登陆点击付费视频文章记录"""
        self.index.clickvideoDetailRecord("1")
        result = self.index.is_clickvideoDetailRecord_success("1")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clicktwLiveFeeRecord
    def test_clicktwLiveFeeRecord(self,index):
        """未登陆点击免费图文直播记录"""
        index.clicktwLiveRecord("0")
        time.sleep(2)
        result= index.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clicktwLiveChargedRecord
    def test_clicktwLiveChargedRecord(self,index):
        """未登陆点击付费图文直播记录"""
        index.clicktwLiveRecord("1")
        result = index.is_clicktwLiveRecord_success("1")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.clickliveVideoFeeRecord
    def test_clickliveVideoFeeRecord(self,index):
        """未登陆点击免费视频直播记录"""
        index.clickliveVideoRecord("0")
        result = index.is_clickliveVideoRecord_success("0")
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.clickliveVideoChargedRecord
    def test_clickliveVideoChargedRecord(self,index):
        """未登陆点击付费视频直播记录"""
        index.clickliveVideoRecord("1")
        result = index.is_nologinclickliveVideoRecord_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clickcourseFeeRecord
    def test_clickcourseFeeRecord(self):
        """未登录点击免费课程"""
        self.index.clickcourse('0')
        result = self.index.is_clickcourse_success('0')
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clickcourseChargedRecord
    def test_clickcourseChargeRecord(self):
        """未登录点击付费课程"""
        #self.index.getCourseNums()
        self.index.clickcourse('1')
        result = self.index.is_clickcourse_success('1')
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clickeliteAdviserRecord
    def test_clickeliteAdviserRecord(self):
        """未登陆精英投顾记录"""
        self.index.clickeliteAdviserRecord()
        result1 = self.index.is_clickeliteAdviserRecordAdviserPicture_success()
        result2 = self.index.is_clickeliteAdviserRecordAdviserName_success()
        result3 = self.index.is_both_true(result1, result2)
        print("result的结果为%s" % result1, result2)
        assert result3



if __name__ == "__main__":
    pytest.main(["-s", "-v","-m=clickliveVideoChargedRecord","--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_nologin.py","--html=./report/report.html","--self-contained-html"])
    #pytest.main(["-s", "-v", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_nologin.py", "--html=./report.html","--self-contained-html"])

    #pytest.main(["-s", "--browser=chrome","--host=https://m.dev.hbec.com", "test_adviser_purchasedAccountLogin.py","--html=./report/report.html","--self-contained-html"])
