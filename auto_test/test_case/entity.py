# -*- coding: utf-8 -*-
"""
@file: entity.py
@desc:
@author: Jaden Wu
@time: 2020/9/22 9:27
"""
from abc import ABCMeta, abstractmethod


class TestCase(metaclass=ABCMeta):
    @abstractmethod
    def precondition(self) -> bool:
        pass

    @abstractmethod
    def body(self) -> bool:
        pass

    @abstractmethod
    def restore_env(self) -> bool:
        pass

    def run(self) -> tuple:
        tc_result = self.precondition() and self.body()
        restore_env_res = self.restore_env()
        return tc_result, restore_env_res
