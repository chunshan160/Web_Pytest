# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 21:37
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : constants.py
# @Software: PyCharm


class Constants:
    browser = "Chrome"
    base_url = "http://8.129.91.152:8765"
    login_url = base_url + "/Index/login.html"
    register_url = base_url + "/Index/reg.html"
    invest_url = base_url + "/loan/finance.html"
    index_url = base_url + "/Index/index"


if __name__ == '__main__':
    print("http://8.129.91.152:8765/Index/login.html")
    print(Constants.login_url)
