#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2021/1/30 15:55
# @Author :春衫
# @File :base_page3.py
import time

import win32con
import win32gui
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.base_test import BaseTest
from Common.logger import UserLog

"""
所有页面对象类的公共操作
"""

log = UserLog().user_log()


class BasePage:

    def wait_element_visible(self, locator, times=30, poll_frequency=0.5):
        """
        等待元素可见
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        times 最长等待时间
        poll_frequency 检查间隔
        Returns 满足可见条件的元素
        -------
        """
        try:
            webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
            return webDriverWait.until(EC.visibility_of_element_located(locator))
        except BaseException  as e:
            log.error(f"等待元素{locator}可见失败")
            log.error(e)

    def wait_elements_visible(self, locator, times=30, poll_frequency=0.5):
        """
        等待所有元素可见
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        times 最长等待时间
        poll_frequency 检查间隔
        Returns 满足可见条件的元素
        -------
        """
        try:
            webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
            return webDriverWait.until(EC.visibility_of_all_elements_located(locator))
        except BaseException  as e:
            log.error(f"等待所有元素{locator}可见失败")
            log.error(e)

    def wait_element_clickable(self, locator, times=30, poll_frequency=0.5):
        """
        等待元素可被点击
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        times 最长等待时间
        poll_frequency 检查间隔
        Returns 满足可被点击条件的元素
        -------
        """
        try:
            webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
            return webDriverWait.until(EC.element_to_be_clickable(locator))
        except BaseException  as e:
            log.error(f"等待元素{locator}可被点击失败")
            log.error(e)

    # def wait_elements_clickable(self,locator, times=30, poll_frequency=0.5):
    #     """
    #     定位到多个元素的情况下，等待指定元素可被点击
    #     Parameters
    #     ----------
    #     locator 元素的定位信息（元素定位方式+定位值）
    #     times 最长等待时间
    #     poll_frequency 检查间隔
    #     Returns 满足可被点击条件的元素
    #     -------
    #     """
    #     webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
    #     return webDriverWait.until(EC.element_to_be_clickable(locator))

    def wait_elePresence(self, locator, times=30, poll_frequency=0.5):
        """
        等待元素存在
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        times 最长等待时间
        poll_frequency 检查间隔
        Returns 满足元素存在条件的元素
        -------
        """
        try:
            webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
            webDriverWait.until(EC.presence_of_element_located(locator))
        except BaseException  as e:
            log.error(f"等待元素{locator}存在失败")
            log.error(e)

    def click(self, locator, desc):
        """
        点击的二次封装
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        Returns
        -------
        """
        log.info(f"【{desc}】,点击元素{locator}")
        self.wait_element_clickable(locator).click()

    def send_keys(self, locator, data, desc):
        """
        输入数据的二次封装
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        data 数据
        Returns
        -------

        """
        log.info(f"往【{desc}】输入数据【{data}】")
        self.wait_element_visible(locator).clear()
        self.wait_element_visible(locator).send_keys(data)

    def send_keys_key(self, locator, key, desc):
        """
        点击按键的二次封装
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        key 按键操作
        Returns
        -------

        """
        log.info(f"往【{desc}】点击按键【{key}】")
        self.wait_element_visible(locator).send_keys(key)


    def get_element_text(self, locator, desc):
        """
        获取元素文本值二次封装
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        Returns
        -------
        """
        text = self.wait_element_visible(locator).text
        log.info(f"获取【{desc}】文本为【{text}】")
        return text

    def js_click(self, locator, desc):
        """
        javaScript点击
        Parameters
        ----------
        locator 元素的定位信息（元素定位方式+定位值）
        Returns
        -------
        """
        js = "arguments[0].click()"
        web_element = self.wait_element_visible(locator)
        BaseTest.driver.execute_script(js, web_element)
        log.info(f"【{desc}】通过js点击了元素{locator}")

    def js_set_attribute(self, attribute, desc):
        js = f'document.getElementById("train_date").setAttribute({attribute})'
        BaseTest.driver.execute_script(js)
        log.info(f"【{desc}】通过js添加了元素属性{attribute}")

    def js_remove_attribute(self, attribute, desc):
        js = f'document.getElementById("train_date").removeAttribute({attribute})'
        BaseTest.driver.execute_script(js)
        log.info(f"【{desc}】通过js移除了元素属性{attribute}")

    """JavaScript滚动"""

    def js_scroll_to_element(self, element):
        """滚动到指定元素位置上"""
        BaseTest.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true)", element)

    def js_scroll_to_top(self):
        """滚动到页面的最底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        BaseTest.driver.execute_script(js)

    def js_scroll_to_bottom(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        BaseTest.driver.execute_script(js)

    def js_scroll(self, x, y):
        """
        Parameters：左右上下滚动
        向上滚动：(0,-500)
        向下滚动：(0,500)
        向左滚动：(-500,0)
        向右滚动：(500,0)
        ----------
        x：X轴，向右越来越大
        y：Y轴，向下越来越大
        Returns：无
        -------
        """

        js = f"window.scrollBy({x},{y})"
        BaseTest.driver.execute_script(js)

    """懒加载"""

    def scroll_load(self, locator, keyword):
        """
        Parameters：滚动到底部自动加载
        ----------
        locator：定位表达式
        keyword：想要寻找的字符串

        Returns：无
        -------

        """
        while True:
            # 滚动之前获取页面的源代码
            beforeSource = BaseTest.driver.page_source
            # 如果找到了元素的情况
            if keyword in beforeSource:
                # 通过JavaScript点击元素
                webElement = BaseTest.driver.find_element(*locator)
                BaseTest.driver.execute_script("arguments[0].click()", webElement)
                # 跳出循环
                break
            time.sleep(0.5)
            # 每一次的滑动操作-都是滚动到页面的最底部，自动触发每一次的懒加载过程
            BaseTest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(0.5)
            # 滚动到底部之后来获取页面的源代码
            afterSource = BaseTest.driver.page_source
            if afterSource == beforeSource:
                print("滑动前后的页面源代码一样，无法加载")
                break

    def click_load(self, locator1, locator2, keyword):
        # 点击更多
        while True:
            # 如果找到了元素的情况
            if keyword in BaseTest.driver.page_source:
                BaseTest.driver.find_element(*locator1).click()
                # 跳出循环
                break
            time.sleep(0.5)
            # 点击之前来获取页面的源代码
            beforeSource = BaseTest.driver.page_source
            # 点击更多

            # # 第一种种方案：判断查看更多按钮是否能被点击，通过try
            # try:
            #     element = BaseTest.driver.find_element(*locator2)
            #     # 滚动到元素位置
            #     BaseTest.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true)", element)
            #     element.click()
            # except:
            #     # 如果捕捉到了异常信息，那么就说明已经到了页面最底部-->退出循环
            #     print("点击更多按钮不能被点击了，页面滑动到了最底部")
            #     break

            # 第二种方案：判断查看更多按钮是否可见
            element = BaseTest.driver.find_element(*locator2)
            if not element.is_displayed():
                print("查看更多按钮不可见的，页面滑动到了最底部")
                break
            element.click()

            # 点击之后来获取页面的源代码
            afterSource = BaseTest.driver.getPageSource()
            if afterSource == beforeSource:
                break
            time.sleep(0.5)

    """select标签"""

    def select_by_index(self, element, index):
        """根据索引值"""
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        """根据value属性"""
        Select(element).select_by_value(value)

    def select_by_visible_text(self, element, text):
        """根据文本"""
        Select(element).select_by_visible_text(text)

    """SwitchAlert"""

    def alert_accept(self):
        # 确认alert弹窗
        alert = BaseTest.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        # 取消alert弹窗
        alert = BaseTest.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        # 获取alert文本
        alert = BaseTest.driver.switch_to.alert
        return alert.text

    """SwitchToIframe"""

    def switch_to_iframe(self, iframe, times=30, poll_frequency=0.5):
        """
        Parameters
        ----------
        iframe：iframe索引/id/name/元素都行
        Returns
        -------
        """
        # iframe切换
        webDriverWait = WebDriverWait(BaseTest.driver, times, poll_frequency)
        webDriverWait.until(EC.frame_to_be_available_and_switch_to_it(iframe))

    def switch_to_parent_frame(self, iframe):
        """切换到父级iframe"""
        BaseTest.driver.switch_to.parent_frame(iframe)

    def switch_to_default_content(self, iframe):
        """回到最顶级页面"""
        BaseTest.driver.switch_to_default_content(iframe)

    """SwitchToWindow"""

    def switch_to_current_window(self):
        """切换到当前最新打开的窗口"""
        # 获取打开的多个窗口句柄
        allHandles = BaseTest.driver.window_handles
        # 切换到当前最新打开的窗口
        BaseTest.driver.switch_to.window(allHandles[-1])

    def switch_to_specify_window(self, url):
        """切换到指定窗口"""
        # 获取打开的多个窗口句柄
        allHandles = BaseTest.driver.window_handles
        # 切换到指定窗口
        for handle in allHandles:
            if BaseTest.driver.current_url == url:
                break
            else:
                BaseTest.driver.switch_to.window(handle)

    # web上传图片
    def web_upload_image(self, filepath, desc):
        try:
            # 一级窗口
            dialog = win32gui.FindWindow("#32770", "打开")
            # 二级窗口
            comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            # 三级窗口
            combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
            # 四级窗口 文本输入框
            edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
            # 打开按钮 二级窗口
            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开")
            # 输入文件路径
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
            # 点击打开按钮 上传文件
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        except BaseException  as e:
            log.error(f"{desc}上传图片失败!")
            log.error(e)
            raise
