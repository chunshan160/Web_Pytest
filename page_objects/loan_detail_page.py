#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 14:52
#@Author :春衫
#@File :loan_detail_page.py

from base.base_page import BasePage
from page_locators import loan_detail_locators as locators

class LoanDetailPage(BasePage):

    def invest(self,amount):
        self.send_keys(locators.invest_amount_input,amount,"项目页面-投资金额输入框")
        self.click(locators.invest_button,"项目页面-投资按钮")


    def get_invest_success_tips(self):
        return self.get_element_text(locators.invest_success_tips,"项目页面-投资成功的提示信息")


    def click_close(self):
        self.js_click(locators.close,"项目页面-投资成功提示框关闭按钮")

