#-*- coding: utf-8 -*-
from selenium import webdriver
from common.base import Base
import time

"""
page/login_page.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
"""

# -------------定位元素信息------------ #
loc_phone = ("xpath", "//*[@id=\"app\"]/div/div[1]/div[1]/div[1]/form/div/div/div/div/div/input")
loc_next = ("xpath", "//*[@id=\"app\"]/div/div[1]/div[1]/div[1]/form/button")
loc_password= ("xpath", "//*[@id=\"app\"]/div/div[1]/form/div[1]/div[1]/div/div[2]/input")
loc_login = ("xpath", "//*[@id=\"app\"]/div/div[1]/form/button")


result_loc = ("xpath", ".//*[@id='userMenu']/a")


def _login(driver, host, user="15900000006", psw="a111111"):
    '''
    登录函数
    '''
    adviser = Base(driver)
    driver.get(host + "/account/login/index.htm?weChatType=aitou&referrer=http://m.dev.hbec.com/adviser/index/main#/")
    adviser.sendKeys(loc_phone, user)
    adviser.click(loc_next)
    adviser.sendKeys(loc_password, psw)
    adviser.click(loc_login)

def _enterPage(driver,host):
    '''
    进入某个页面
    '''
    Base(driver)
    driver.get(host + "/adviser/index/main")
    driver.maximize_window()

def _login_result(driver, _text):
    '''
    登录成功后，获取当前页面的用户名，判断用户名
    :param driver:
    :param _text: 用户名
    :return: True or False
    '''
    zen = Base(driver)
    r = zen.is_text_in_element(result_loc, _text)
    return r


def _get_alert(driver):
    '''判断alert在不在,存在返回text文本内容，不存在返回空字符'''
    zen = Base(driver)
    try:
        alert = zen.is_alert()
        text = alert.text
        alert.accept()  # 点alert确定
        return text
    except:
        return ""


if __name__ == "__main__":
    chromedriver = "D:\myWebdriver\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.maximize_window()
    _enterPage(browser, "https://m.dev.hbec.com")
