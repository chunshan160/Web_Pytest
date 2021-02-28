#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2021/1/28 14:39
# @Author :春衫
# @File :test_invest.py

import allure
import pytest

from Common.base_test import BaseTest
from PageObjects.index_page import IndexPage
from PageObjects.loan_detail_page import LoanDetailPage
from PageObjects.login_page import LoginPage
from PageObjects.member_info_page import MemberInfoPage
from TestData.login_data import login_success_data


@allure.feature('投标功能')
class TestInvest(BaseTest):

    # def setup_class(self):
    #     BaseTest().open_browser("Chrome")
    #     BaseTest().to_url(Constants.login_url)
    #
    # def teardown_class(self):
    #     # 后置
    #     BaseTest().close_browser()

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("mobile_phone,password", login_success_data)  # 替代ddt
    def test_invest(self, mobile_phone, password):
        # 1、登录
        with allure.step("登录"):
            LoginPage().login(mobile_phone, password)
        # 投资之前获取用户的可用余额
        with allure.step("投资之前获取用户的可用余额"):
            IndexPage().click_my_account()
            beforeAmount = MemberInfoPage().get_leave_amount_text()
        # 2、投资
        with allure.step("投资"):
            self.back_url()
            IndexPage().click_bid_button()
            LoanDetailPage().invest("1000")
        # 断言
        # 1、根据弹窗的提示文本
        actual = LoanDetailPage().get_invest_success_tips()
        with allure.step("断言投标成功弹窗提示文本"):
            assert actual == "投标成功！","投标成功弹窗提示文本错误"
        # 2、用户的余额减少了这么多
        # 拿投资之前的金额和投资之后的金额相减？？
        LoanDetailPage().click_close()
        IndexPage().click_my_account()
        afterAmount = MemberInfoPage().get_leave_amount_text()
        actual = float(beforeAmount[:-1]) - float(afterAmount[:-1])
        with allure.step("断言投标前后账户余额"):
            assert actual == 1000,"投标前后账户余额对不上"
