# -*- coding: utf-8 -*-
"""
@file: test_tc_app.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 15:27
"""
from auto_test.use_cases.tc_app import TCApp
from auto_test.use_cases.interfaces.repository_if import TCRepoIf
from auto_test.use_cases.interfaces.output_port_if import PresenterIf


class TCRepo(TCRepoIf):
    def save(self, testcase: dict) -> int:
        return 1


class Presenter(PresenterIf):
    def set_tc_info(self, tc_info):
        pass


tc_app = TCApp(TCRepo(), Presenter())


def test_add_testcase():
    assert tc_app.add_testcase(
        lambda: True,
        lambda: True,
        lambda: True,
        {}
    ) is True
