#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 11:48
#@Author :春衫
#@File :index_page.py

from Common.base_page import BasePage
from PageLocators import index_locators as locators

class IndexPage(BasePage):

    """获取我的账户元素文本信息"""
    def get_my_account_text(self):
        return self.get_element_text(locators.my_account,"主页页面-我的账户元素")

    """点击我的账户"""
    def click_my_account(self):
        self.click(locators.my_account,"主页页面-我的账户元素")

    """点击抢投标"""
    def click_bid_button(self):
        # waitElementsVisible(bidButtonBy).get(0).click()
        self.click(locators.bid_button,"主页页面-抢投标元素")