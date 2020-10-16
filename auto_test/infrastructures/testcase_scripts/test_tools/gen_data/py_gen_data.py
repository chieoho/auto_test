# -*- coding: utf-8 -*-
"""
@file: py_gen_data.py
@desc:
@author: Jaden Wu
@time: 2020/9/22 11:41
"""
from auto_test.infrastructures.testcase_scripts.test_tools.gen_data import GenData


class PyGenData(GenData):
    def __init__(self):
        pass

    def gen_data(self) -> bool:
        print('python gen data')
        return True
