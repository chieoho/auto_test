# -*- coding: utf-8 -*-
"""
@file: _interface.py
@desc:
@author: Jaden Wu
@time: 2020/9/22 11:36
"""
from abc import ABCMeta, abstractmethod


class GenData(metaclass=ABCMeta):
    @abstractmethod
    def gen_data(self) -> bool:
        pass
