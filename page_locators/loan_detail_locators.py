#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2021/1/28 14:53
# @Author :春衫
# @File :loan_detail_locators.py

from selenium.webdriver.common.by import By

# 投资金额的输入框
invest_amount_input = (By.XPATH, "//input[@data-url='/Invest/invest']")
# 投标的按钮
invest_button = (By.XPATH, "//button[text()='投标']")
# 投资成功弹窗的成功提示
invest_success_tips = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")
# 关闭
close = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='close_pop']")
