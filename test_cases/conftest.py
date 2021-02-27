#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py

import os
import sys
import allure
import pytest

sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
from base.base_test import BaseTest
from Conf.constants import Constants


# 登录前置后置
@pytest.fixture(scope='class')
def login():
    BaseTest().open_browser(Constants.browser)
    BaseTest().to_url(Constants.login_url)
    yield
    BaseTest().close_browser()


# pytest执行失败自动截图并添加到allure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # mode = "a" if os.path.exists("failures") else "w"
        # with open("failures", mode) as f:
        #     # let's also access a fixture for the fun of it
        #     if "tmpdir" in item.fixturenames:
        #         extra = " (%s)" % item.funcargs["tmpdir"]
        #     else:
        #         extra = ""
        #     f.write(rep.nodeid + extra + "\n")
        # # 添加allure报告截图
        # # if hasattr(driver, "get_screenshot_as_png"):
        with allure.step('添加失败截图...'):
            allure.attach(BaseTest.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
