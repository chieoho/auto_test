# -*- coding: utf-8 -*-
"""
@file: test_tc_app.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 15:27
"""
from auto_test.use_cases.tc_app import TCApp
from auto_test.use_cases.interfaces.output_port_if import TCRepoIf


class TCRepoImp(TCRepoIf):
    def save(self, testcase: dict) -> int:
        return 1


tc_app = TCApp(TCRepoImp())


def test_add_testcase():
    assert tc_app.add_testcase(
        lambda: True,
        lambda: True,
        lambda: True,
        {}
    ) is True
