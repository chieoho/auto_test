# -*- coding: utf-8 -*-
"""
@file: testcase.py
@desc:
@author: Jaden Wu
@time: 2020/10/12 9:37
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class TCEntity(metaclass=ABCMeta):
    """
    testcase entity
    """

