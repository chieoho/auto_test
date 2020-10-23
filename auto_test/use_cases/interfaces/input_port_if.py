# -*- coding: utf-8 -*-
"""
@file: input_port_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/22 16:14
"""
from abc import ABCMeta, abstractmethod


class TCAppIf(metaclass=ABCMeta):
    """
    testcase input port interface
    """
    @abstractmethod
    def add_testcase(
            self,
            precondition: callable,
            body: callable,
            restore_env: callable,
            tc_info_in: dict
    ) -> bool:
        """
        添加用例
        :param precondition:
        :param body:
        :param restore_env:
        :param tc_info_in:
        :return:
        """
