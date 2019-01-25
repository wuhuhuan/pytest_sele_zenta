# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
"""
page/add_bug_page.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
"""

class AddBugPage(Base):  # 继承Base

    # 添加BUG
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_truck = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换iframe
    loc_input_body = ("class name", "article-content")
    loc_avse = ("css selector", "#submit")

    # 新增的列表
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, title="测试提交BUG"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title, title)
        # 输入body
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        # 富文本不能clear
        body = '''[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_input_body, body)
        self.driver.switch_to.default_content()

        self.click(self.loc_avse)

    def is_add_bug_sucess(self):
        return self.findElement(self.loc_new)

if __name__ == "__main__":
    from page.login_page import _login
    driver = webdriver.Firefox()
    _login(driver, "http://127.0.0.1")

    bug = AddBugPage(driver)
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交BUG"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_sucess(title)
    print(result)







