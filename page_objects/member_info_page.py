#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 14:45
#@Author :春衫
#@File :member_info_page.py

from base.base_page import BasePage
from page_locators import member_info_locators as locators

class MemberInfoPage(BasePage):

    def get_leave_amount_text(self):
        return self.get_element_text(locators.leave_amount,"个人信息页面-可用余额")
