# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 16:41
# @Author  : wuhuhuan
# @Email   :472406662@touker.com
# @File    : test_liveLIst.py
# @Software: PyCharm
import pytest
import time
class TestliveList:
    @pytest.mark.test_clickAll_liveList
    def test_clickAll_liveList(self,livelist):
        '''看直播页-点击全部筛选按钮'''
        livelist.clickAll()
        #livelist.get_titles()
        assert livelist.is_AllSort_success()
    @pytest.mark.clickLiving_liveList
    def test_clickLiving_liveList(self,livelist):
        '''看直播页-点击全部-正在直播筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickLiving()
        assert livelist.is_livingSort_success()

    @pytest.mark.clickPlayback_liveList
    def test_clickPlayback_liveList(self,livelist):
        '''看直播页-点击全部-回放筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickPlayback()
        assert livelist.is_playbackSort_success()

    @pytest.mark.clickAboutToLive_liveList
    def test_clickAboutToLive_liveList(self,livelist):
        '''看直播页-点击全部-即将直播筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickAboutToLive()
        assert livelist.is_AboutToLiveSort_success()
    @pytest.mark.clickHottest_liveList
    def test_clickHottest_liveList(self,livelist):
        '''看直播页-点击最热筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickHottest()
        assert livelist.is_hotTestSort_success()
    @pytest.mark.clickAdviserAll_liveList
    def test_clickAdviserAll_liveList(self,livelist):
        '''看直播页-点击投顾-全部筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickAdviserAll()
        assert livelist.is_adviserAllSort_success()
    @pytest.mark.clickyuwei_liveList
    def test_clickyuwei_liveList(self,livelist):
        '''看直播页-点击投顾-虞伟筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickyuwei()
        assert livelist.is_yuweiSort_success()
    @pytest.mark.clickdengming_liveList
    def test_clickdengming_liveList(self,livelist):
        '''看直播页-点击投顾-邓明筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickdengming()
        assert livelist.is_dengmingSort_success()
    @pytest.mark.clickchengbang_liveList
    def test_clickchengbang_liveList(self,livelist):
        '''看直播页-点击投顾-陈邦筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickchenbang()
        assert livelist.is_chenbangSort_success()
    @pytest.mark.clicklujiachen_liveList
    def test_clicklujiachen_liveList(self,livelist):
        '''看直播页-点击投顾-陆佳辰筛选按钮'''
        livelist.js_scroll_top()
        livelist.clicklujiachen()
        assert livelist.is_lujiachenSort_success()
    @pytest.mark.clickhuabaotougu_liveList
    def test_clickhuabaotougu_liveList(self,livelist):
        '''看直播页-点击投顾-华宝投顾筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickhuabaotougu()
        assert livelist.is_huabaotouguSort_success()
    @pytest.mark.clickOther_liveList
    def test_clickOther_liveList(self,livelist):
        '''看直播页-点击投顾-华宝投顾筛选按钮'''
        livelist.js_scroll_top()
        livelist.clickOther()
        assert livelist.is_otherSort_success()
    @pytest.mark.clickTimetable_liveList
    def test_clickTimetable_liveList(self,livelist):
        '''看直播页-点击投顾-华宝投顾筛选按钮'''
        livelist.clickTimetable()
        assert livelist.is_clickTimetable_success()

    @pytest.mark.clicktwLiveFeeRecord_liveList
    def test_clicktwLiveFeeRecord_liveList(self,livelist):
        """看直播页-未登陆点击免费图文直播记录"""
        livelist.clicktwLiveRecord("0")
        result= livelist.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.clicktwLiveChargedRecord_liveList
    def test_clicktwLiveChargedRecord_liveList(self,livelist):
        """看直播页-未登陆点击付费图文直播记录"""
        livelist.clicktwLiveRecord("1")
        result = livelist.is_clicktwLiveRecord_success("1")
        print("result的结果为%s" % result)
        assert result


    @pytest.mark.clickliveVideoFeeRecord_liveList
    def test_clickliveVideoFeeRecord_liveList(self,livelist):
        """看直播页-未登陆点击免费视频直播记录"""
        livelist.clickliveVideoRecord("0")
        result = livelist.is_clickliveVideoRecord_success("0")
        print("result的结果为%s" % result)
        assert result



    @pytest.mark.clickliveVideoChargedRecord_liveList
    def test_clickliveVideoChargedRecord_liveList(self,livelist):
        """看直播页-未登陆点击付费视频直播记录"""
        livelist.clickliveVideoRecord("1")
        result = livelist.is_nologinclickliveVideoRecord_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.clicktwLiveFeeLoginRecord_liveList
    def test_clicktwLiveFeeLoginRecord_liveList(self,livelist):
        """看直播页-已登陆点击免费图文直播记录"""
        livelist.clicktwLiveRecord("0")
        result = livelist.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.clicktwLiveChargedLoginRecord_liveList
    def test_clicktwLiveChargedLoginRecord_liveList(self,livelist):
        """看直播页-已登陆点击付费图文直播记录"""
        livelist.clicktwLiveRecord("1")
        result = livelist.is_clicktwLiveRecord_success("1")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginclickliveFeeVideRecord_liveList
    def test_openedAccountLoginclickliveFeeVideRecord_liveList(self,livelist):
        """看直播页-已登录点击免费视频直播记录"""
        livelist.clickliveVideoRecord("0")
        result = livelist.is_clickliveVideoRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("openedAccountLogin")
    @pytest.mark.openedAccountLoginclickliveChargedVideRecord_liveList
    def test_openedAccountLoginclickliveChargedVideRecord_liveList(self,livelist):
        """看直播页-已登录点击付费视频直播记录"""
        livelist.clickliveVideoRecord("1")
        result = livelist.is_clickliveVideoRecord_success("1")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("purchasedAccountLogin")
    @pytest.mark.purchasedAccountLoginclicktwLiveChargedRecord_liveList
    def test_purchasedAccountLoginclicktwLiveChargedRecord_liveList(self,livelist):
        """看直播页-已购买点击付费图文直播记录"""
        livelist.clicktwLiveRecord("1")
        result = livelist.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("purchasedAccountLogin")
    @pytest.mark.purchasedAccountLoginclickliveChargedVideoRecord_liveList
    def test_purchasedAccountLoginclickliveChargedVideoRecord_liveList(self,livelist):
        """看直播页-已购买登录点击付费视频直播记录"""
        livelist.clickliveVideoRecord("1")
        result = livelist.is_clickliveVideopurchasedRecord_success()
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginclicktwLiveFeeLoginRecord_liveList
    def test_unopenedAccountLoginclicktwLiveFeeLoginRecord_liveList(self,livelist):
        """看直播页-未开户点击免费图文直播记录"""
        livelist.clicktwLiveRecord("0")
        result = livelist.is_clicktwLiveRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginclicktwLiveChargedLoginRecord_liveList
    def test_unopenedAccountLoginclicktwLiveChargedLoginRecord_liveList(self,livelist):
        """看直播页-未开户点击付费图文直播记录"""
        livelist.clicktwLiveRecord("1")
        result = livelist.is_clicktwLiveRecord_success("1")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginclickliveFeeVideRecord_liveList
    def test_unopenedAccountLoginclickliveFeeVideRecord_liveList(self,livelist):
        """看直播页-未开户点击免费视频直播记录"""
        livelist.clickliveVideoRecord("0")
        result = livelist.is_clickliveVideoRecord_success("0")
        print("result的结果为%s" % result)
        assert result

    @pytest.mark.usefixtures("unopenedAccountLogin")
    @pytest.mark.unopenedAccountLoginclickliveChargedVideRecord_liveList
    def test_unopenedAccountLoginclickliveChargedVideRecord_liveList(self,livelist):
        """看直播页-未开户点击付费视频直播记录"""
        livelist.clickliveVideoRecord("1")
        result = livelist.is_clickliveVideoUnopenedRecord_success()
        print("result的结果为%s" % result)
        assert result



if __name__=="__main__":
    pytest.main(["-s", "-v","-m","unopenedAccountLoginclickliveChargedVideRecord_liveList","--browser=chrome","--host=https://m.dev.hbec.com", "test_liveList.py","--html=./report/report.html","--self-contained-html"])
    #pytest.main(["-s", "-v","--browser=chrome","--host=https://m.dev.hbec.com", "test_liveList.py","--html=./report/report.html","--self-contained-html"])
