#coding:utf-8
from selenium import webdriver
from common.base import Base
import pytest
import time
class TestAddBug():

    @pytest.mark.usefixtures("login")  # 先登录
    def test_add_bug(self, driver):
        a =4
        b=5
        assert a==b

if __name__=="__main__":
    pytest.main(["-s","--browser=chrome","test_login222.py","--html=./report/report.html"])