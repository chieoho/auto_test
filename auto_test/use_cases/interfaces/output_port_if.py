# -*- coding: utf-8 -*-
"""
@file: output_port_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/27 15:51
"""
from abc import ABCMeta, abstractmethod


class PresenterIf(metaclass=ABCMeta):
    @abstractmethod
    def set_tc_info(self, tc_info):
        """
        设置用例信息为可展示格式
        :return:
        """