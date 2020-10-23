# -*- coding: utf-8 -*-
"""
@file: output_port_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/22 16:26
"""
from abc import ABCMeta, abstractmethod


class TCRepoIf(metaclass=ABCMeta):
    """
    testcase output port interface
    """
    @abstractmethod
    def save(self, testcase: dict) -> int:
        """
        存储用例
        :param testcase:
        :return:
        """
