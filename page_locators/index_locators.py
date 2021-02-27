#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 11:49
#@Author :春衫
#@File :index_locators.py

from selenium.webdriver.common.by import By

#我的账户元素
my_account =(By.XPATH,"//a[contains(text(),'我的帐户')]")
#抢投标元素
bid_button = (By.XPATH,"//a[text()='抢投标']")