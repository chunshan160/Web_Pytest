#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py

from selenium.webdriver.common.by import By

# 手机号码输入框
mobile_phone = (By.NAME, "phone")
# 密码输入框
pwd = (By.XPATH, "//input[@placeholder='密码']")
# 登录按钮
login = (By.XPATH, "//button[text()='登录']")
# 输入框的提示信息
input_tips = (By.XPATH, "//div[@class='form-error-info']")
