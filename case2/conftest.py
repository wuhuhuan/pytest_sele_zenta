#coding:utf-8
import pytest
from page.login_page import _login

"""
case/conftest.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
登录功能调用
"""

@pytest.fixture()
def openedAccountLogin(driver, host):
    """已开户登录功能fixture"""
    _login(driver, host)
    yield
    driver.delete_all_cookies()

@pytest.fixture()
def unopenedAccountLogin(driver, host):
    """未开户登录功能fixture"""
    _login(driver, host,user="17888888888", psw="111111b")
    yield
    driver.delete_all_cookies()


