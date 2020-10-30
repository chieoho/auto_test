# -*- coding: utf-8 -*-
"""
@file: output_port_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/27 15:51
"""
from abc import ABCMeta, abstractmethod


class TCPresenter(metaclass=ABCMeta):
    @abstractmethod
    def add_tc(self):
        """
        增加测试用例的返回结果展示
        :return:
        """