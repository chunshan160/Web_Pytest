#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 11:07
#@Author :春衫
#@File :base_test.py

from selenium import webdriver

from base.log import UserLog
from base.project_path import chrome_driver_path

"""
BaseTest是所有测试用例类的父类
"""

log=UserLog().user_log()
class BaseTest:
    # 驱动能够被其他地方使用到（全局可以共享）
    driver = None

    """根据浏览器名字打开对应的浏览器"""
    def open_browser(self,browser_name):
        if browser_name == 'Firefox':
            BaseTest.driver = webdriver.Firefox(executable_path=chrome_driver_path)
            log.info("=====================打开了Firefox浏览器===================")
        elif browser_name == 'Chrome':
            BaseTest.driver = webdriver.Chrome(executable_path=chrome_driver_path)
            log.info("=====================打开了Chrome浏览器===================")
        elif browser_name == 'IE':
            BaseTest.driver = webdriver.Ie(executable_path=chrome_driver_path)
            log.info("=====================打开了IE浏览器===================")
        BaseTest.driver.maximize_window()
        # driver.implicitly_wait(10)
        # print(driver)
        # return driver

    def to_url(self,url):
        """跳转到对应的网址"""
        BaseTest.driver.get(url)

    def get_current_url(self):
        """获取当前网页的URL地址"""
        return BaseTest.driver.current_url

    def back_url(self):
        """浏览器后退"""
        BaseTest.driver.back()

    def forward_url(self):
        """浏览器前进"""
        BaseTest.driver.forward()

    def refresh_url(self):
        """浏览器刷新"""
        BaseTest.driver.refresh()

    def close_browser(self):
        """关闭浏览器"""
        BaseTest.driver.quit()
        log.info("=====================关闭了浏览器===================")

if __name__ == '__main__':
    BaseTest().open_browser('Chrome')
    print(BaseTest.driver)
    BaseTest().close_browser()