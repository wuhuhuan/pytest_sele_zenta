#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
'''
page/adviserMain.py文件
** 作者：上海-吴沪欢
'''
class adviserMain(Base):
    # 点击页面元素
    # 点击找投顾
    loc_FindAdviserButton_1 = ('xpath', '//*[@id="left-type"]/a')
    loc_FindAdviserButton_2 = ('xpath', '/html/body/div/div[2]/div[1]/div[10]')
    #看直播按钮
    loc_liveButton_1=('xpath','//*[@id="left-type"]/div[1]/a')
    loc_liveButton_2 = ('xpath', '/html/body/div/div[3]/div[6]')
    #跟操作按钮
    loc_findPortfolioButton_1=('xpath', '//*[@id="left-type"]/div[2]/a')
    loc_findPortfolioButton_2 = ('xpath', '/html/body/div[1]/div[2]/div[1]')
    #知观点按钮
    loc_ViewpointListButton_1 = ('xpath', '//*[@id="left-type"]/div[3]/a')
    loc_ViewpointListButton_2 = ('xpath', '/html/body/div[1]/div/div[2]/div[6]')
    #学课程按钮
    loc_CourseButton_1 = ('xpath', '//*[@id="left-type"]/div[4]/a')
    loc_CourseButton_2 = ('xpath', '/html/body/div[1]/div[2]/div[3]')
    #问个股按钮
    loc_QuestionButton_1 = ('xpath', '//*[@id="left-type"]/div[5]/a')
    loc_QuestionButton_2 = ('xpath', '/html/body/div[1]/div[3]/div[10]')
    #模拟盘更多按钮
    loc_findPortfolioMoreButton_1=('xpath', '/html/body/div[1]/div[2]/div/div[3]/a')
    loc_findPortfolioMoreButton_2= ('xpath', '/html/body/div[1]/div[2]/div[1]')
    # 直播更多按钮
    loc_liveMoreButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[7]/a')
    loc_liveMoreButton_2 = ('xpath', '/html/body/div/div[3]/div[6]')
    #观点更多按钮
    loc_ViewpointListMoreButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[5]/a')
    loc_ViewpointListMoreButton_2 = ('xpath', '/html/body/div[1]/div/div[2]/div[6]')
    #课程更多按钮
    loc_CourseMoreButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[9]/a')
    loc_CourseMoreButton_2 = ('xpath', '/html/body/div[1]/div[2]/div[3]')
    #精英投顾更多
    loc_eliteAdviserMoreButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[11]/a')
    loc_eliteAdviserMoreButton_2 = ('xpath', '/html/body/div[1]/div/div[7]')
    #点击模拟盘记录
    targetPortfolioNums = []
    ordinaryPortfolios = []
    feePortfolios = []
    loc_targetFindPortfolioRecordButton= ('xpath',   '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[1]')
    loc_ordinaryFindPortfolioRecordButton= ('xpath',   '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[1]')
    loc_feeFindPortfolioRecordButton = ('xpath',   '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[1]')
    loc_NotLogin = ('xpath', '//*[@id=\"loginf\"]')
    NotLoggedInext="立即登录"
    loc_unopenedAccountLogin=('xpath', '//*[@id=\"stockopen\"]')
    unopenedAccountLogintext = "立即开户"
    loc_openedAccountLogin = ('xpath', '//*[@id=\"mimicplaDiv\"]/div[7]/span')
    openedAccountLogintext = "组合持仓"



    # 未登陆点击投顾信息
    loc_findPortfolioRecordAdviserButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]')
    loc_findPortfolioAdviserPicture_1= ('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]/span[1]/img')
    loc_findPortfolioAdviserName_1=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]/span[2]')
    loc_taIndexAdviserPicture_1=('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/a/img')
    loc_taIndexAdviserName_1 = ('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a')
    adviserName=''
    adviserPicture=''
    #未登录点击观点文章
    loc_indexViewpointRecord_1=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[1]')
    loc_indexViewpointAdviserPicture_1=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[1]/div/a/span[1]/img')
    loc_indexViewpointAdviserName_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[1]/div/a/span[2]')
    loc_viewpointDetailAdviserName_1 = ('xpath', '/html/body/div/div[2]/div[2]/p[1]')
    loc_viewpointDetailAdviserPicture_1 = ('xpath', '/html/body/div/div[2]/div[1]/img')
    indexViewpointAdviserName = ''
    indexViewpointAdviserPicture= ''

    #点击视频文章记录
    loc_videoDetailRecord_1=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[2]')
    loc_videoDetailRecord_2 = ('xpath', '/html/body/div[2]/div[1]/div[2]/span')
    videoDetailRecordText='推荐视频'

    # 点击图文直播记录
    loc_twLiveRecord_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[1]')
    loc_twLiveDetail_1 = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/p/span[1]')
    twLiveDetailText = '主讲'

    # 点击视频直播记录
    loc_liveVideoRecord_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[2]')
    loc_liveVideoRecordTitle_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[2]/div[2]/div[1]')
    loc_liveVideoDetailTitle_1 = ('xpath','/html/body/div[3]/div[4]/div[2]/div[1]/div[1]/span')
    liveVideoRecordTitle=''

    #点击免费课程
    loc_courseFee_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[10]/div[1]/a')
    loc_courseDetailFee_1= ('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/dvi[2]')
    courseFeeText='试看'

    #点击精英投顾记录
    loc_eliteAdviserRecord_1= ('xpath', '/html/body/div[1]/div[2]/div/div[12]/div[1]')
    loc_eliteAdviserRecordAdviserName_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[12]/div[1]/div[1]/div[2]/p[1]')
    loc_eliteAdviserRecordAdviserPicture_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[12]/div[1]/div[1]/div[1]/img')
    loc_eliteAdvisertaIndexAdviserName_1 = ('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a')
    loc_eliteAdvisertaIndexAdviserPicture_1 = ('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/a/img')
    eliteAdvisertaIndexAdviserName= ''
    eliteAdvisertaIndexAdviserPicture = ''

    #栏目文案定位
    loc_menuid_1=("id","/html/body/div[1]/div[2]/div/div[3]/span[2]")
    loc_menuid_2 =("id", "/html/body/div[1]/div[2]/div/div[5]/span[2]")
    loc_menuid_3 = ("id", "/html/body/div[1]/div[2]/div/div[7]/span[2]")
    loc_menuid_4 = ("id", "/html/body/div[1]/div[2]/div/div[9]/span[2]")

    # 栏目文案测试数据
    test_menuid_data = [
        (loc_menuid_1, "选股择时，省时省心"),
        (loc_menuid_2, "每日文章，洞悉市场"),
        (loc_menuid_3, "直面投顾，即时交流"),
        (loc_menuid_4, "系统学习，进阶投资")
    ]
    #百度定位
    loc_input_content=("id","kw")
    loc_input_id=("id","su")

    def baidu(self,content):
        time.sleep(2)
        self.sendKeys(self.loc_input_content,content)
        self.click(self.loc_input_id)
    # 获取模拟盘属性值
    def getPortfolioNums(self):
        """aa"""
        eles = self.findElements(("xpath", "//div[contains(@class, 'stock-item')]"))
        i = 0
        for ele in eles:
            text = str(ele.get_attribute("class"))
            print("属性值为：%s" % text)
            i = i + 1
            if text == 'stock-item com_tips_aim':
                print("stock-item com_tips_aim:%s" % text)
                self.targetPortfolioNums.append(i)

            elif text == 'stock-item com_tips':
                print("stock-item com_tips:%s" % text)
                self.ordinaryPortfolios.append(i)
            else:
                print("stock-item:%s" % text)
                self.feePortfolios.append(i)
        for targetPortfolioNum in self.targetPortfolioNums:
            print("targetPortfolioNum的值为：%s" % targetPortfolioNum)
        for ordinaryPortfolio in self.ordinaryPortfolios:
            print("ordinaryPortfolio的值为：%s" % ordinaryPortfolio)
        for feePortfolio in self.feePortfolios:
            print("feePortfolio的值为：%s" % feePortfolio)
            "/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[1]"
        self.loc_targetFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.targetPortfolioNums[0]) + ']/a[1]')
        self.loc_ordinaryFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.ordinaryPortfolios[0]) + ']/a[1]')
        self.loc_feeFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.feePortfolios[0]) + ']/a[1]')
        return self.loc_targetFindPortfolioRecordButton,self.loc_ordinaryFindPortfolioRecordButton,self.loc_feeFindPortfolioRecordButton
    def gettest_menuid_data(self):
        return self.test_menuid_data
    def clickFindAdviserButton(self):
        self.click(self.loc_FindAdviserButton_1)

    def is_clickFindAdviserButton_sucess(self):
        return self.findElement(self.loc_FindAdviserButton_2)

    def clickliveButton(self):
        self.click(self.loc_liveButton_1)
    def is_clickliveButton_sucess(self):
        return self.findElement(self.loc_liveButton_2)

    def clickfindPortfolioButton(self):
        self.click(self.loc_findPortfolioButton_1)
    def is_clickfindPortfolioButton_sucess(self):
        return self.findElement(self.loc_findPortfolioButton_2)

    def clickViewpointListButton(self):
        self.click(self.loc_ViewpointListButton_1)
    def is_clickViewpointListButton_sucess(self):
        return self.findElement(self.loc_ViewpointListButton_2)

    def clickCourseButton(self):
        self.click(self.loc_CourseButton_1)
    def is_clickCourseButton_sucess(self):
        return self.findElement(self.loc_CourseButton_2)

    def clickQuestionButton(self):
        self.click(self.loc_QuestionButton_1)
    def is_clickQuestionButton_sucess(self):
        return self.findElement(self.loc_QuestionButton_2)

    def clickfindPortfolioMoreButton(self):
        self.click(self.loc_findPortfolioMoreButton_1)
    def is_clickfindPortfolioMoreButton_success(self):
        return self.findElement(self.loc_findPortfolioMoreButton_2)

    def clickliveMoreButton(self):
        self.click(self.loc_liveMoreButton_1)
    def is_clickliveMoreButton_sucess(self):
        return self.findElement(self.loc_liveMoreButton_2)

    def clickViewpointListMoreButton(self):
        self.click(self.loc_ViewpointListMoreButton_1)
    def is_clickViewpointListMoreButton_sucess(self):
        return self.findElement(self.loc_ViewpointListMoreButton_2)

    def clickCourseMoreButton(self):
        self.click(self.loc_CourseMoreButton_1)
    def is_clickCourseMoreButton_success(self):
        return self.findElement(self.loc_CourseMoreButton_2)

    def clickeliteAdviserMoreButton(self):
        self.click(self.loc_eliteAdviserMoreButton_1)
    def is_clickeliteAdviserMoreButton_success(self):
        return self.findElement(self.loc_eliteAdviserMoreButton_2)

    # 点击模拟盘记录
    def clickfindPortfolioRecordButton(self,sign):

        if sign==1:
            self.click(self.loc_targetFindPortfolioRecordButton)
        elif sign==2:
            self.click(self.loc_ordinaryFindPortfolioRecordButton)
        elif sign==3:
            self.click(self.loc_feeFindPortfolioRecordButton)
        else:
            print("不符合参数，sign：1、目标付费模拟盘、2、普通付费模拟盘3、免费模拟盘")
    def is_clickfindPortfolioRecordButton_success(self,sign):
        if sign==1:
            self.js_scroll_end()
            return self.is_text_in_element(self.loc_NotLogin,self.NotLoggedInext)
        elif sign==2:
            self.js_scroll_end()
            return self.is_text_in_element(self.loc_unopenedAccountLogin, self.unopenedAccountLogintext)
        elif sign==3:
            self.js_scroll_end()
            return self.is_text_in_element(self.loc_openedAccountLogin, self.openedAccountLogintext)
        else:
            print("不符合参数，sign：1未登录、2、未开户账号登录3、开户账号登录")

    # 未登陆点击模拟盘投顾信息
    def clickfindPortfolioRecordAdviserButton(self):
        self.adviserName = self.findElement(self.loc_findPortfolioAdviserName_1).text
        self.adviserPicture = self.findElement(self.loc_findPortfolioAdviserPicture_1).get_attribute("src")
        self.click(self.loc_findPortfolioRecordAdviserButton_1)
    def is_clickfindPortfoliotaIndexAdviserPicture_success(self):
        return self.is_text_in_element_attribute(self.loc_taIndexAdviserPicture_1, self.adviserPicture)

    def is_clickfindPortfoliotaIndexAdviserName_success(self):
        return self.is_text_in_element(self.loc_taIndexAdviserName_1, self.adviserName)

    # 未登陆点击文章记录
    def clickviewpointRecord(self):
        self.indexViewpointAdviserName = self.findElement(self.loc_indexViewpointAdviserName_1).text
        self.indexViewpointAdviserPicture = self.findElement(self.loc_indexViewpointAdviserPicture_1).get_attribute("src")
        self.click(self.loc_indexViewpointRecord_1)

    def is_clickviewpointRecordAdviserPicture_success(self):
        return self.is_text_in_element_attribute(self.loc_viewpointDetailAdviserPicture_1, self.indexViewpointAdviserPicture)

    def is_clickviewpointRecordAdviserName_success(self):
        return self.is_text_in_element(self.loc_viewpointDetailAdviserName_1, self.indexViewpointAdviserName)

    # 未登陆点击视频文章记录
    def clickvideoDetailRecord(self):
        self.click(self.loc_videoDetailRecord_1)

    def is_clickvideoDetailRecord_success(self):
        return self.is_text_in_element(self.loc_videoDetailRecord_2, self.videoDetailRecordText)

    # 未登陆点击图文直播记录
    def clicktwLiveRecord(self):
        self.click(self.loc_twLiveRecord_1)

    def is_clicktwLiveRecord_success(self):
        return self.is_text_in_element(self.loc_twLiveDetail_1, self.twLiveDetailText)

    # 未登陆点击视频直播记录
    def clickliveVideoRecord(self):
        self.click(self.loc_liveVideoRecord_1)
        self.liveVideoRecordTitle=self.get_text(self.loc_liveVideoRecordTitle_1)

    def is_clickliveVideoRecord_success(self):
        return self.is_text_in_element(self.loc_liveVideoDetailTitle_1, self.liveVideoRecordTitle)

    # 点击免费课程

    def clickcourseFee(self):
        self.click(self.loc_courseFee_1)

    def is_clickcourseFee_success(self):
        return self.is_text_in_element(self.loc_courseDetailFee_1, self.courseFeeText)

    # 未登陆精英投顾记录
    def clickeliteAdviserRecord(self):
        self.eliteAdvisertaIndexAdviserName = self.findElement(self.loc_eliteAdviserRecordAdviserName_1).text
        self.eliteAdvisertaIndexAdviserPicture = self.findElement(self.loc_eliteAdviserRecordAdviserPicture_1).get_attribute("src")
        self.click(self.loc_eliteAdviserRecord_1)

    def is_clickeliteAdviserRecordAdviserPicture_success(self):
        return self.is_text_in_element_attribute(self.loc_eliteAdvisertaIndexAdviserPicture_1,
                                                 self.eliteAdvisertaIndexAdviserPicture)

    def is_clickeliteAdviserRecordAdviserName_success(self):
        return self.is_text_in_element(self.loc_eliteAdvisertaIndexAdviserName_1, self.eliteAdvisertaIndexAdviserName)
    #验证栏目文案
    def menuidAdviser(self,loc):
        t1 = self.hou.get_text(loc)
        return t1



if __name__ == "__main__":
    from page.login_page import _enterPage
    chromedriver = "D:\myWebdriver\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()
    _enterPage(driver,"https://m.dev.hbec.com","/adviser/index/main")
    bug = adviserMain(driver)
    bug.clickFindAdviserButton()
    result = bug.is_clickFindAdviserButton_sucess("")
    print(result)