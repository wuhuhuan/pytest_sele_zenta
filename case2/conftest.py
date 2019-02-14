#coding:utf-8
import pytest
from case2.text import Text
from page.login_page import _login
from page.adviserMain import adviserMain
from page.liveList_page import LiveList
from page.weekCourseList_page import WeekCourseList
url_index ="/adviser/index/main"
aaa=None
url_livelist ="/adviser/index/liveList"
url_weekCourseList="/adviser/index/weekCourseList.htm"
"""
case/conftest.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
登录功能调用
"""

@pytest.fixture()
def openedAccountLogin(driver, host):
    """已开户登录功能fixture"""
    _login(driver, host)


@pytest.fixture()
def unopenedAccountLogin(driver, host):
    """未开户登录功能fixture"""
    _login(driver, host,user="17888888888", psw="111111b")


@pytest.fixture()
def purchasedAccountLogin(driver, host):
    """未开户登录功能fixture"""
    _login(driver, host,user="15900000007", psw="a111111")
    yield
    # driver.delete_all_cookies()

# @pytest.fixture(scope='session')
# def index(driver,host):
#     '''初始化'''
#     index = adviserMain(driver)
#     index.getPortfolioNums
#     driver.maximize_window()
#     driver.get(host + url_index)
#     return index

@pytest.fixture(scope='session')
def livelist(driver,host):
    '''初始化'''
    livelist=LiveList(driver)
    driver.maximize_window()
    driver.get(host + url_livelist)
    return livelist
# @pytest.fixture(scope='session')
# def weekCourseList(driver,host):
#     '''初始化'''
#     weekCourseList=WeekCourseList(driver)
#     driver.maximize_window()
#     driver.get(host + url_weekCourseList)
#     return weekCourseList
# @pytest.fixture(scope='session')
# def param():
#     '''初始化'''
#     aa = Text()
#     param= aa.getCourseText()
#     return param

