#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2021/1/27 22:27
# @Author :春衫
# @File :login_page.py

from page_locators import login_locators as locators
from base.base_page import BasePage


class LoginPage(BasePage):

    """登录的操作"""
    def login(self, mobilephone, pwd):
        self.send_keys(locators.mobile_phone, mobilephone,"登录页面-手机号码输入框")
        self.send_keys(locators.pwd, pwd,"登录页面-密码输入框")
        self.click(locators.login,"登录页面-登录按钮")

    """获取输入框提示信息的文本值"""
    def get_input_tips_text(self):
        return self.get_element_text(locators.input_tips,"登录页面-输入框提示信息")
