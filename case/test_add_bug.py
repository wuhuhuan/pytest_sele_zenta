#coding:utf-8
from page.add_bug_page import AddBugPage
import pytest
import time

"""
case/test_add_bug.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
添加bug功能流程
"""

class TestAddBug():

    @pytest.mark.usefixtures("login")  # 先登录
    def test_add_bug(self, driver):
        """测试添加BUG流程"""
        bug = AddBugPage(driver)
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交BUG"+timestr
        bug.add_bug(title)
        result = bug.is_add_bug_sucess(title)
        print("测试结果：%s" % result)
        assert result

if __name__ == "__main__":
    pytest.main(["-s", "test_add_bug.py"])