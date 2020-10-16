# -*- coding: utf-8 -*-
"""
@file: tc_for_unittest_001.py
@desc: 给单元测试用的脚本
@author: Jaden Wu
@time: 2020/10/16 17:03
"""
from auto_test.adapters.interfaces.tcs_if import TCSBase


class TestCaseScript(TCSBase):
    """
    单元测试用
    """
    def __init__(self):
        super().__init__()

    def precondition(self):
        return True

    def body(self):
        return True

    def restore_env(self):
        return True
