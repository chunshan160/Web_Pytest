# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 14:54
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : test_login.py
# @Software: PyCharm

import pytest
import allure

from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from base.base_test import BaseTest
from test_data.login_data import login_success_data
from test_data.login_data import login_failure_datas
from Conf.constants import Constants


@allure.feature('登录功能')
class TestLogin(BaseTest):

    # def setup_class(self):
    #     BaseTest().open_browser("Chrome")
    #     BaseTest().to_url(Constants.login_url)
    #
    # def teardown_class(self):
    #     # 后置
    #     BaseTest().close_browser()

    @allure.story("异常登录")
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("mobile_phone,password,expected", login_failure_datas)  # 替代ddt
    def test_login_failure(self, mobile_phone, password, expected):
        with allure.step("登录"):
            LoginPage().login(mobile_phone, password)
        # 断言 - -根据输入框的提示信息
        actualValue = LoginPage().get_input_tips_text()
        with allure.step("断言输入框的提示信息"):
            assert actualValue == expected, "登录异常输入框提示错误"

    @allure.story("正常登录")
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("mobile_phone,password", login_success_data)  # 替代ddt
    def test_login_success(self, mobile_phone, password):
        with allure.step("登录"):
            LoginPage().login(mobile_phone, password)
        # 断言 期望结果和实际结果是否相同
        # 1、账户昵称是否为自动化测试帐号1
        actual = IndexPage().get_my_account_text()
        with allure.step("断言登录账户"):
            assert actual == "我的帐户[自动化测试帐号1]", "正常登录账户信息错误"
        # 2、跳转到首页
        actualUrl = self.get_current_url()
        with allure.step("断言跳转页面"):
            assert actualUrl == Constants.index_url
