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
from Common.logger import UserLog
from Common.base_test import BaseTest
from Common.constants import Constants

log = UserLog().user_log()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='class', autouse=True)
def browser():
    BaseTest().open_browser(Constants.browser)


# 登录前置后置
@pytest.fixture(scope='class')
def login():
    BaseTest().to_url(Constants.login_url)
    yield
    BaseTest().close_browser()


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    :param item:
    :param call:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # mode = "a" if os.path.exists("failures") else "w"
        # with open("failures", mode)as f:
        #     if "tmpir" in item.fixturenames:
        #         extra = " (%s)" % item.funcargs["tmpdir"]
        #     else:
        #         extra = ""
        #     # f.write(report.nodeid + extra + "\n")
        with allure.step('执行失败截图'):
            allure.attach(BaseTest.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
