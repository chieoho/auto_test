# -*- coding: utf-8 -*-
"""
@file: tc_adapter_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/14 16:49
"""
from abc import ABCMeta, abstractmethod
from auto_test.entities.tc_entity import TCEntity


class TCAdapter(metaclass=ABCMeta):
    """
    testcase adapter interface
    """
    @abstractmethod
    def get(self, case_id: int) -> TCEntity:
        pass

    @abstractmethod
    def save(self, testcase: TCEntity) -> bool:
        pass

    @abstractmethod
    def mark(self, case_id: int) -> bool:
        pass

    @abstractmethod
    def delete(self, case_id: int) -> bool:
        pass
