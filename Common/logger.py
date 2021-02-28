#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/19 19:03
# @Author :春衫
# @File :Logs.py

import logging

from Common.dir_config import log_conf_path, log_path
from Common.read_yaml import read_yaml


class UserLog:

    def user_log(self):
        config = read_yaml(log_conf_path)
        # 收集
        logger_collect_level = config['logger_collect_level']
        # 打印
        logger_print_level = config['logger_print_level']
        # 输出
        logger_output_level = config['logger_output_level']

        # 定义一个日志收集器my_logger
        logger = logging.getLogger('春衫')

        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not logger.handlers:
            # 设置级别 全收集
            logger.setLevel(logger_collect_level)

            # 设置输出格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息:%(message)s')

            # 创建一个输出渠道 打印级别
            sh = logging.StreamHandler()
            sh.setLevel(logger_print_level)
            sh.setFormatter(formatter)

            # 日志文件名格式
            log_file = "web_auto" + ".logs"
            log_name = log_path + "/" + log_file

            # 创建日志文件 写入级别
            fh = logging.FileHandler(log_name, encoding='utf-8')
            fh.setLevel(logger_output_level)
            fh.setFormatter(formatter)

            # 收集输出对接
            logger.addHandler(sh)
            logger.addHandler(fh)

            # 关闭日志收集器(渠道)
            sh.close()
            fh.close()
            # logger.removeHandler(sh)
            # logger.removeHandler(fh)

        return logger


if __name__ == '__main__':
    logger = UserLog().user_log()
    logger.debug('测试')
    logger.info('测试')
    # UserLog().user_log('测试一下1', 'ERROR')
    # UserLog().user_log('测试一下2', 'ERROR')
