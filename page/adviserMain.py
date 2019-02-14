#-*- coding: utf-8 -*-
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
    #---未开户定位
    loc_unopenedAccountLogin=('xpath', '//*[@id=\"stockopen\"]')
    unopenedAccountLogintext = "立即开户"
    #已购买定位
    loc_purchased = ('xpath', '//*[@id=\"mimicplaDiv\"]/div[7]/span')
    purchasedText = "组合持仓"
    #未购买定位
    loc_openedAccountLogin = ('xpath', '//*[@id=\"mimicplaDiv\"]/div[14]/a[2]')
    openedAccountLogintext = "免费查看"



    # 未登陆点击投顾信息
    loc_findPortfolioRecordAdviserButton_1 = ('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]')
    loc_findPortfolioAdviserPicture_1= ('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]/span[1]/img')
    loc_findPortfolioAdviserName_1=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/a[2]/span[2]')
    loc_taIndexAdviserPicture_1=('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/a/img')
    loc_taIndexAdviserName_1 = ('xpath', '/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a')
    adviserName=''
    adviserPicture=''
    #未登录点击免费观点文章
    indexViewpointfeeNums=[]
    loc_indexViewpointFeeRecord=('xpath', '/ddd')
    loc_indexViewpointAdviserPicture_1=('xpath', '/ccc')
    loc_indexViewpointAdviserName_1 = ('xpath', '/bbb')
    loc_viewpointDetailAdviserName_1 = ('xpath', '/html/body/div[1]/div[3]/div[2]/p[1]')
    loc_viewpointDetailAdviserPicture_1 = ('xpath', '/html/body/div[1]/div[3]/div[1]/img')
    indexViewpointAdviserName = ''
    indexViewpointAdviserPicture= ''

    # 未登录点击付费观点文章
    indexViewpointChargedNums = []
    loc_indexViewpointChargedRecord= ('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[1]')
    loc_indexViewpoint = ('xpath', '/html/body/div[1]/div[7]/a[2]')
    indexViewpointText= '免费查看'




    #点击视频文章记录
    indexVideoViewpointChargedNums=[]
    indexVideoViewpointFeeNums = []
    loc_videoDetailfeeRecord=('xpath', '//ddfdfdf')
    loc_videoDetailChargedRecord = ('xpath', '//ddfd33fdf')
    loc_indexViewpointChargedRecord = ('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[1]')
    loc_videoDetailfeeRecord_1 = ('xpath', '/html/body/div[2]/div[1]/div[2]/span')
    videoDetailRecordText_1='推荐视频'
    loc_videoDetailfeeRecord_2 = ('xpath', '//*[@class=\'modal-btn confirm undefined\']')
    videoDetailRecordText_2 = '购买'

    # 点击图文直播记录
    twLiveRecordfeeNums=[]
    twLiveRecordChargedNums = []
    loc_twLiveFeeRecord= ('xpath', '/dfdfd')
    loc_twLiveChargedRecord = ('xpath', '/dfdfdww')
    loc_twLivefeeDetail= ('xpath', '//span[@data-type=\'Zj\']')
    twLiveFeeDetailText = '主讲'
    loc_twLiveChargedDetail = ('xpath', '/html/body/div[1]/div[2]/div/a')
    twLiveChargedDetailText = '付费购买'

    # 点击视频直播记录
    liveVideoFeeRecord=[]
    liveVideoChargedRecord=[]
    loc_liveVideoFeeRecord = ('xpath', '/ccddee')
    loc_liveVideoChargedRecord = ('xpath', '/ccddee')
    loc_liveVideoFeeRecordTitle = ('xpath', '/cc')
    loc_liveVideoChargedRecordTitle= ('xpath', '/charged')
    loc_liveVideoDetailTitle = ('xpath','/html/body/div[3]/div[4]/div[2]/div[1]/div[1]/span')
    liveVideoFeeRecordTitle=''
    liveVideoChargedRecordTitle=''
    loc_liveVideoChargedRecord_1 = ('xpath', '//*[@id="buy"]')
    liveVideoChargedRecordText='购买'
    loc_liveVideoChargedunopenedRecord=('xpath', '//*[@id=\"agentForm\"]/div[1]/div[2]/div[2]/span/a')
    liveVideoChargedunopenedRecordText='《华宝证券网上开户约定协议》'


    #未登录通用定位判断

    loc_unlogin=('xpath','//*[@id=\"app\"]/div/div[1]/div[1]/div[1]/div')
    unloginText='手机号登录'



    #点击免费课程
    courseFeeNums = []
    loc_courseFee= ('xpath', '/bbb/')
    loc_courseDetailFee= ('xpath', '/html/body/div[1]/div[1]/div[4]/div[2]')
    courseFeeText='内容列表'
    #点击付费课程
    courseChargedNums=[]
    loc_courseCharged = ('xpath', '/aaa/')
    loc_courseDetailCharged = ('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[2]/a[2]')
    courseChargedText = '免费查看'

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

    # 获取直播属性值
    def getLiveNums(self):
        """aa"""
        eles = self.findElements(("xpath", "//div[contains(@class, 'liveItem item com-href')]"))
        i = 0
        for ele in eles:
            text = str(ele.get_attribute("class"))
            print("属性值为：%s" % text)
            i = i + 1
            #图文直播付费
            if text == 'liveItem item com-href  com_tips':
                print("liveItem item com-href  com_tips:%s" % text)
                self.twLiveRecordChargedNums.append(i)
            #图文直播不付费
            elif text == 'liveItem item com-href ':
                print("liveItem item com-href:%s" % text)
                self.twLiveRecordfeeNums.append(i)
            #视频直播付费
            elif text == 'liveItem item com-href video com_tips':
                self.liveVideoChargedRecord.append(i)
            #视频直播不付费
            elif text == 'liveItem item com-href video':
                self.liveVideoFeeRecord.append(i)
            else:
                print("无效的直播class定位：%s"%text)

        for twLiveRecordfeeNum in self.twLiveRecordfeeNums:
            print("twLiveRecordfeeNum：%s" % twLiveRecordfeeNum)
    #直播对应定位信息
    def getliveElement(self,locMethod,head,end,sign):
        #图文免费记录
        if sign==1:
            self.loc_twLiveFeeRecord=(str(locMethod), str(head) + str(self.twLiveRecordfeeNums[0]) + str(end))
            return self.loc_twLiveFeeRecord
            #return self.loc_twLiveFeeRecord=('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.twLiveRecordfeeNums[0]) + ']/div[1]/img')
        #图文直播付费
        elif sign ==2:
            #self.loc_twLiveChargedRecord = ('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.twLiveRecordChargedNums[0]) + ']/div[1]/img')
            self.loc_twLiveChargedRecord = (str(locMethod), str(head) + str(self.twLiveRecordChargedNums[0]) + str(end))
            return self.loc_twLiveChargedRecord
        # 视频直播不付费
        elif sign ==3:
            #self.loc_liveVideoFeeRecord=('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.liveVideoFeeRecord[0]) + ']/div[2]')
            self.loc_liveVideoFeeRecord = (str(locMethod), str(head) + str(self.liveVideoFeeRecord[0]) + str(end))
            return self.loc_liveVideoFeeRecord
        # 视频直播付费
        elif sign ==4:
            #self.loc_liveVideoChargedRecord=('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.liveVideoChargedRecord[0]) + ']/div[2]')
            self.loc_liveVideoChargedRecord = (str(locMethod), str(head) + str(self.liveVideoChargedRecord[0]) + str(end))
            return self.loc_liveVideoChargedRecord
        # 视频直播不付费预期结果
        elif sign==5:
            #self.loc_liveVideoFeeRecordTitle=('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.liveVideoFeeRecord[0]) + ']/div[2]/div[1]')
            self.loc_liveVideoFeeRecordTitle = (str(locMethod), str(head) + str(self.liveVideoFeeRecord[0]) + str(end))
            return self.loc_liveVideoFeeRecordTitle
        #视频直播付费预期结果
        elif sign==6:
            #self.loc_liveVideoChargedRecordTitle = ('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' + str(self.liveVideoChargedRecord[0]) + ']/div[2]/div[1]')
            self.loc_liveVideoChargedRecordTitle = (str(locMethod), str(head) + str(self.liveVideoChargedRecord[0]) + str(end))
            return self.loc_liveVideoChargedRecordTitle

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
        self.loc_targetFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.targetPortfolioNums[0]) + ']/a[1]')
        self.loc_ordinaryFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.ordinaryPortfolios[0]) + ']/a[1]')
        self.loc_feeFindPortfolioRecordButton=('xpath', '/html/body/div[1]/div[2]/div/div[4]/div/div[' + str(self.feePortfolios[0]) + ']/a[1]')
        return self.loc_targetFindPortfolioRecordButton,self.loc_ordinaryFindPortfolioRecordButton,self.loc_feeFindPortfolioRecordButton

    # 获取文章属性值
    def getArticleNums(self):
        """aa"""
        eles = self.findElements(("xpath", "//div[contains(@data-url, 'articleId=')]"))
        i = 0
        for ele in eles:
            i = i + 1
            text = str(ele.get_attribute("class"))
            text2 = ("xpath", "/html/body/div[1]/div[2]/div/div[6]/div[" + str(i) + "]/p[2]")
            if self.findElement(text2):
                text1=self.findElement(text2).get_attribute("class")
            else:
                text1=""
            print("属性值为：%s" % text)
            if text == 'item com-href':
                if text1=="view-content":
                    print("item com-href:%s" % text)
                    print("view-content:%s" % text1)
                    self.indexViewpointfeeNums.append(i)
                elif text1=="view-pic":
                    self.indexVideoViewpointFeeNums.append(i)
                    print("item com-href:%s" % text)
                    print("view-pic:%s" % text1)
                else:
                    print("没有找到文章和视频内容定位")
            elif text == 'item com-href com_tips':
                if text1 == "view-content":
                    print("item com-href com_tips:%s" % text)
                    self.indexViewpointChargedNums.append(i)
                elif text1 == "view-pic":
                    self.indexVideoViewpointChargedNums.append(i)
                    print("item com-href com_tips:%s" % text)
                    print("view-pic:%s" % text1)
            else:
                print("都没有找到%s" % text)
        print(u"免费文章数："+str(self.indexViewpointfeeNums[0]),u"收费文章数："+str(self.indexViewpointChargedNums[0]),
              u"免费视频文章数：" +str(self.indexVideoViewpointFeeNums[0]),u"付费视频文章数：" +str(self.indexVideoViewpointChargedNums[0]))
        self.loc_indexViewpointFeeRecord = ( 'xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexViewpointfeeNums[0]) + ']')
        self.loc_indexViewpointChargedRecord = ('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexViewpointChargedNums[0]) + ']')
        try:
            self.loc_videoDetailfeeRecord=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexVideoViewpointFeeNums[0]) + ']')
        except IndexError, e:
            print e.message

        try:
            self.loc_videoDetailChargedRecord=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexVideoViewpointChargedNums[0]) + ']')
        except IndexError, e:
            print e.message
        self.loc_indexViewpointAdviserName_1=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexViewpointfeeNums[0]) + ']/div/a/span[2]')
        self.loc_indexViewpointAdviserPicture_1=('xpath', '/html/body/div[1]/div[2]/div/div[6]/div[' + str(self.indexViewpointfeeNums[0]) + ']/div/a/span[1]/img')
    # 获取课程属性值
    def getCourseNums(self):
        """aa"""
        eles = self.findElements(("xpath", "//div[contains(@class, 'course-list-item')]"))
        i = 0
        for ele in eles:
            text = str(ele.get_attribute("class"))
            print("属性值为：%s" % text)
            i = i + 1
            locs=("xpath","/html/body/div[1]/div[2]/div/div[10]/div["+str(i)+"]/a/div[2]")
            if self.findElement(locs):
                className = str(self.findElement(locs).get_attribute("class"))
                if className=="toll-icon":
                    self.courseChargedNums.append(i)
                else:
                    print("不是付费课程的i值为：%s" % i)
                    self.courseFeeNums.append(i)
        self.loc_courseCharged = ('xpath', '/html/body/div[1]/div[2]/div/div[10]/div['+str(self.courseChargedNums[0])+']/a')
        self.loc_courseFee=('xpath', '/html/body/div[1]/div[2]/div/div[10]/div['+str(self.courseFeeNums[0])+']/a')


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
        elif sign==4:
            self.js_scroll_end()
            return self.is_text_in_element(self.loc_purchased, self.purchasedText)
        else:
            print("不符合参数，sign：1未登录、2、未开户账号登录3、已购买登录4、")

    # 未登陆点击模拟盘投顾信息
    def clickfindPortfolioRecordAdviserButton(self):
        self.adviserName = self.findElement(self.loc_findPortfolioAdviserName_1).text
        self.adviserPicture = self.findElement(self.loc_findPortfolioAdviserPicture_1).get_attribute("src")
        self.click(self.loc_findPortfolioRecordAdviserButton_1)
    def is_clickfindPortfoliotaIndexAdviserPicture_success(self):
        return self.is_text_in_element_attribute(self.loc_taIndexAdviserPicture_1, self.adviserPicture)

    def is_clickfindPortfoliotaIndexAdviserName_success(self):
        return self.is_text_in_element(self.loc_taIndexAdviserName_1, self.adviserName)

    # 点击文章记录
    def clickviewpointRecord(self,sign):
        self.getArticleNums()
        self.indexViewpointAdviserName = self.findElement(self.loc_indexViewpointAdviserName_1).text
        self.indexViewpointAdviserPicture = self.findElement(self.loc_indexViewpointAdviserPicture_1).get_attribute("src")
        if sign=='0':
            self.click(self.loc_indexViewpointFeeRecord)
        elif sign=='1':
            self.click(self.loc_indexViewpointChargedRecord)
        else:
            print("不符合参数，sign：0 ：免费、1:：付费")

    def is_clickviewpointRecordAdviserPicture_success(self):
        return self.is_text_in_element_attribute(self.loc_viewpointDetailAdviserPicture_1, self.indexViewpointAdviserPicture)

    def is_clickviewpointRecordAdviserName_success(self):
        return self.is_text_in_element(self.loc_viewpointDetailAdviserName_1, self.indexViewpointAdviserName)

    def is_clickviewpointRecord_success(self):
        return self.is_text_in_element(self.loc_indexViewpoint, self.indexViewpointText)
    def is_clickviewpointRecord_Reverse(self):
        return self.is_text_in_elementReverse(self.loc_indexViewpoint, self.indexViewpointText)

    # 未登陆点击视频文章记录
    def clickvideoDetailRecord(self,sign):
        self.getArticleNums()
        if sign=='0':
            self.click(self.loc_videoDetailfeeRecord)
        elif sign=='1':
            self.click(self.loc_videoDetailChargedRecord)
        else:
            print("不符合参数，sign：0、免费视频文章、1、收费视频文章")

    def is_clickvideoDetailRecord_success(self,sign):
        if  sign =="0":
            return self.is_text_in_element(self.loc_videoDetailfeeRecord_1, self.videoDetailRecordText_1)
        elif sign =="1":
            #self.switch_alert()
            return self.is_text_in_element(self.loc_videoDetailfeeRecord_2, self.videoDetailRecordText_2)

    #通用点击判断付费收费
    def clickMethod(self,sign,feeLoc,chargedLoc,feeComment,chargedComment):
        if sign == "0":
            self.click(feeLoc)
        elif sign == "1":
            self.click(chargedLoc)
        else:
            print("不符合参数，sign：0:"+feeComment+"1:"+chargedComment)
    #通用判断付费和免费是否成功
    def is_success(self,sign,feeLoc,feeExpect,chargedLoc,chargedExpect,feeComment,chargedComment):
        if sign == "0":
            return self.is_text_in_element(feeLoc, feeExpect)
        elif sign == "1":
            return self.is_text_in_element(chargedLoc,chargedExpect)
        else:
            print("不符合参数，sign：0:" + feeComment + "1:" + chargedComment)
            return False
    # 未登陆点击图文直播记录
    def clicktwLiveRecord(self,sign):
        self.js_scroll_end()
        self.getLiveNums()
        self.clickMethod(sign,self.getliveElement('xpath','/html/body/div[1]/div[2]/div/div[8]/div[',']/div[1]/img',1),self.getliveElement('xpath','/html/body/div[1]/div[2]/div/div[8]/div[',']/div[1]/img',2),"免费图文直播","付费图文直播")

    def is_clicktwLiveRecord_success(self,sign):
        return self.is_success(sign,self.loc_twLivefeeDetail,self.twLiveFeeDetailText,self.loc_twLiveChargedDetail,self.twLiveChargedDetailText,"免费图文直播","付费图文直播")

    # 未登陆点击视频直播记录
    def clickliveVideoRecord(self,sign):
        self.js_scroll_end()
        self.getLiveNums()
        self.liveVideoFeeRecordTitle = self.get_text(self.getliveElement('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[', ']/div[2]/div[1]',5))
        self.liveVideoChargedRecordTitle = self.get_text(self.getliveElement('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' , ']/div[2]/div[1]',6))
        self.clickMethod(sign,self.getliveElement('xpath','/html/body/div[1]/div[2]/div/div[8]/div[',']/div[2]',3),self.getliveElement('xpath', '/html/body/div[1]/div[2]/div/div[8]/div[' , ']/div[2]',4),"免费视频直播","付费视频直播")


    def is_clickliveVideoRecord_success(self,sign):
        return self.is_success(sign, self.loc_liveVideoDetailTitle, self.liveVideoFeeRecordTitle, self.loc_liveVideoChargedRecord_1,self.liveVideoChargedRecordText, "免费图文直播", "付费图文直播")

    def is_clickliveVideoUnopenedRecord_success(self):
        return self.is_text_in_element(self.loc_liveVideoChargedunopenedRecord,self.liveVideoChargedunopenedRecordText)


    def is_nologinclickliveVideoRecord_success(self):
        return self.is_text_in_element(self.loc_unlogin,self.unloginText)

    def is_clickliveVideopurchasedRecord_success(self):
        return self.is_text_in_element(self.loc_liveVideoDetailTitle, self.liveVideoChargedRecordTitle)
    # 点击免费课程

    def clickcourse(self,sign):
        self.getCourseNums()
        if sign=='0':
            self.click(self.loc_courseFee)
        elif sign == '1':
            self.click(self.loc_courseCharged)
        else:
            print("不符合参数，sign：0、免费课程、1、收费课程")


    def is_clickcourse_success(self,sign):
        if sign == '0':
            return self.is_text_in_element(self.loc_courseDetailFee, self.courseFeeText)
        elif sign == '1':
            return self.is_text_in_element(self.loc_courseDetailCharged, self.courseChargedText)
        else:
            print("不符合参数，sign：0、免费课程、1、收费课程")
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
    _enterPage(driver,"https://m.dev.hbec.com")
    bug = adviserMain(driver)
    bug.clickFindAdviserButton()
    result = bug.is_clickFindAdviserButton_sucess("")
    print(result)