# -*- coding: utf-8 -*-
"""
@file: repositories_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 10:27
"""
from abc import ABCMeta, abstractmethod


class TCRepo(metaclass=ABCMeta):
    """
    testcase repository interface
    """
    @abstractmethod
    def get(self, tc_id: int) -> dict:
        pass

    @abstractmethod
    def save(self, testcase: dict) -> int:
        pass

    @abstractmethod
    def update(self, tc_id: int, tc_info: dict) -> bool:
        pass

    @abstractmethod
    def delete(self, tc_id: int) -> bool:
        pass
