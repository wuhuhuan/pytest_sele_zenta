# -*- coding: utf-8 -*-
from common.base import Base
from page.adviserMain import adviserMain
from common.TESTDB import sqled
import time
from selenium import webdriver


class LiveList(Base):
    advisermain=None
    def __init__(self,driver):
        #super(liveList, self).__init__(driver)
        self.timeout = 10
        self.t = 0.5
        self.driver = driver
        self.advisermain=adviserMain(driver)
    sqle = sqled('10.0.30.59', "adviser", "123123", "iadb", 3306, "utf8")
    # sql数据
    loc_all_sql = "select comment from tg_live_menu where checked !=2   order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_living_sql = "select comment from tg_live_menu where checked !=2 and live_islive=1 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_playback_sql = "select comment from tg_live_menu where checked !=2 and live_islive=5 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_AboutToLive_sql = "select comment from tg_live_menu where checked !=2 and live_islive=2 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_hotTest_sql = "select comment from tg_live_menu where checked !=2 and live_islive!=2 order by readcount desc,createdate "
    loc_yuwei_sql = "select comment from tg_live_menu where checked !=2 and adviserid=1021 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_dengming_sql = "select comment from tg_live_menu where checked !=2 and adviserid=1705 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_chenbang_sql = "select comment from tg_live_menu where checked !=2 and adviserid=1708 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_lujiachen_sql = "select comment from tg_live_menu where checked !=2 and adviserid=1660 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_huabaotougu_sql = "select comment from tg_live_menu where checked !=2 and adviserid=1242 order by live_islive asc,live_endtime desc,live_starttime asc"
    loc_other_sql = "select comment from tg_live_menu where checked !=2 and adviserid not in (1242,1021,1705,1708,1660) order by live_islive asc,live_endtime desc,live_starttime asc"
    # 筛选 全部定位
    loc_status = ("xpath", "/html/body/div/div[1]/ul/li[1]")
    statusText = ("xpath", '/html/body/div/div[1]/ul/li[1]/span')
    loc_all = ("xpath", '/html/body/div/div[1]/div/div[1]/div/li[1]')
    loc_living = ("xpath", '/html/body/div/div[1]/div/div[1]/div/li[2]')
    loc_playback = ("xpath", "//li[contains(@data-type, '5')]")
    loc_AboutToLive = ("xpath", '/html/body/div/div[1]/div/div[1]/div/li[4]')
    loc_alls = ("xpath", "//div[contains(@class, 'tit')]")
    # 筛选 最热定位
    loc_hotTest = ("xpath", '/html/body/div/div[1]/ul/li[2]')
    # 筛选 投顾定位
    loc_adviser = ("xpath", '/html/body/div/div[1]/ul/li[3]')
    loc_adviser_all = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[1]')
    loc_yuwei = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[2]')
    loc_dengming = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[3]')
    loc_chenbang = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[4]')
    loc_lujiacheng = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[5]')
    loc_huabaotougu = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[6]')
    loc_other = ("xpath", '/html/body/div/div[1]/div/div[2]/ul/li[7]')
    # 直播课表定位
    loc_Timetable = ("xpath", '/html/body/div/div[1]/a')
    loc_weekCourseList = ("xpath", '/html/body/div/div[2]/div[1]/div[1]')
    weekCourseListText = '周一'
    # 找到更多定位
    loc_more = ("xpath", "//span[contains(@class, 'msg')]")

    def get_expectTitle(self, expectSql):
        aaa = self.sqle.sql(expectSql)
        print("type:-------%s" % type(aaa))
        return aaa

    # 点击全部筛选按钮
    def clickAll(self):
        self.click(self.loc_status)
        self.click(self.loc_all)
        self.js_scroll_end_all1(self.loc_more)

    # 点击正在直播筛选按钮
    def clickLiving(self):
        self.click(self.loc_status)
        self.click(self.loc_living)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击回放筛选按钮
    def clickPlayback(self):
        self.click(self.loc_status)
        self.click(self.loc_playback)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击即将直播筛选按钮
    def clickAboutToLive(self):
        self.click(self.loc_status)
        self.click(self.loc_AboutToLive)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击最热筛选按钮
    def clickHottest(self):
        self.click(self.loc_hotTest)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-全部按钮
    def clickAdviserAll(self):
        self.click(self.loc_adviser)
        self.click(self.loc_adviser_all)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-虞伟按钮
    def clickyuwei(self):
        self.click(self.loc_adviser)
        self.click(self.loc_yuwei)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-邓明按钮
    def clickdengming(self):
        self.click(self.loc_adviser)
        self.click(self.loc_dengming)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-陈邦按钮
    def clickchenbang(self):
        self.click(self.loc_adviser)
        self.click(self.loc_chenbang)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-陆佳辰按钮
    def clicklujiachen(self):
        self.click(self.loc_adviser)
        self.click(self.loc_lujiacheng)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-华宝投顾按钮
    def clickhuabaotougu(self):
        self.click(self.loc_adviser)
        self.click(self.loc_huabaotougu)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击投顾-其他按钮
    def clickOther(self):
        self.click(self.loc_adviser)
        self.click(self.loc_other)
        time.sleep(1)
        self.js_scroll_end_all1(self.loc_more)

    # 点击直播课表按钮
    def clickTimetable(self):
        self.click(self.loc_Timetable)

    def is_clickTimetable_success(self):
        result = self.is_text_in_element(self.loc_weekCourseList, self.weekCourseListText)
        return result

    def is_clickAll_success(self):
        self.is_text_in_element(self.loc_status, self.statusText)

    def get_titles(self):
        self.titles = self.get_tuple_text(self.loc_alls)
        print len(self.titles)
        return self.titles

    # 全部排序
    def is_AllSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_all_sql), self.get_titles())
        return result

    # 正在直播排序
    def is_livingSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_living_sql), self.get_titles())
        return result

    # 回放排序
    def is_playbackSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_playback_sql), self.get_titles())
        return result

    # 即将播放排序
    def is_AboutToLiveSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_AboutToLive_sql), self.get_titles())
        return result

    # 最热排序
    def is_hotTestSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_hotTest_sql), self.get_titles())
        return result

    # 投顾-全部排序
    def is_adviserAllSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_all_sql), self.get_titles())
        return result

    # 投顾-虞伟排序
    def is_yuweiSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_yuwei_sql), self.get_titles())
        return result

    # 投顾-邓明排序
    def is_dengmingSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_dengming_sql), self.get_titles())
        return result

    # 投顾-邓明排序
    def is_chenbangSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_chenbang_sql), self.get_titles())
        return result

    # 投顾-陆佳辰排序
    def is_lujiachenSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_lujiachen_sql), self.get_titles())
        return result

    # 投顾-华宝投顾排序
    def is_huabaotouguSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_huabaotougu_sql), self.get_titles())
        return result

    # 投顾-其他排序
    def is_otherSort_success(self):
        result = self.compare_list_sucess(self.get_expectTitle(self.loc_other_sql), self.get_titles())
        return result
    # 点击视频记录
    def clicktwLiveRecord(self,sign):
        self.js_scroll_end()
        self.advisermain.getLiveNums()
        self.advisermain.clickMethod(sign,self.advisermain.getliveElement('xpath','/html/body/div/div[3]/div[',']/div[1]/img',1),self.advisermain.getliveElement('xpath','/html/body/div/div[3]/div[',']/div[1]/img',2),"免费图文直播","付费图文直播")

    # 判断点击视频记录是否成功
    def is_clicktwLiveRecord_success(self,sign):
        result=self.advisermain.is_clicktwLiveRecord_success(sign)
        return result

    # 未登陆点击视频直播记录
    def clickliveVideoRecord(self, sign):
        self.js_scroll_end()
        self.advisermain.getLiveNums()
        self.liveVideoFeeRecordTitle = self.get_text(self.advisermain.getliveElement('xpath', '/html/body/div/div[3]/div[', ']/div[2]/div[1]', 5))
        self.liveVideoChargedRecordTitle = self.get_text(self.advisermain.getliveElement('xpath', '/html/body/div/div[3]/div[', ']/div[2]/div[1]', 6))
        self.advisermain.clickMethod(sign, self.advisermain.getliveElement('xpath', '/html/body/div/div[3]/div[', ']/div[2]', 3),self.advisermain.getliveElement('xpath', '/html/body/div/div[3]/div[', ']/div[2]', 4),"免费视频直播", "付费视频直播")

    def is_clickliveVideoRecord_success(self,sign):
        result=self.advisermain.is_clickliveVideoRecord_success(sign)
        return result
    def is_nologinclickliveVideoRecord_success(self):
        result=self.advisermain.is_nologinclickliveVideoRecord_success()
        return result

    def is_clickliveVideopurchasedRecord_success(self):
        result = self.advisermain.is_clickliveVideopurchasedRecord_success()
        return result

    def is_clickliveVideoUnopenedRecord_success(self):
        result=self.advisermain.is_clickliveVideoUnopenedRecord_success()
        return result

if __name__ == "__main__":
    chromedriver = "D:\myWebdriver\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    a = liveList(driver)
