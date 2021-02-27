#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2021/1/28 15:28
#@Author :春衫
#@File :common_page.py

from page_locators import common_locators as locators

class CommonPage:

    def go_to_index(self,driver):
        driver.find_element(*locators.index).click()