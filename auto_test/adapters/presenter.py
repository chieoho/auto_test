# -*- coding: utf-8 -*-
"""
@file: presenter.py
@desc:
@author: Jaden Wu
@time: 2020/11/4 13:39
"""
from auto_test.use_cases.interfaces.output_port_if import PresenterIf


class ViewModel(object):
    def __init__(self):
        self.tc_info = {

        }


class Presenter(PresenterIf):
    def __init__(self, model: ViewModel):
        self.model = model

    def set_tc_info(self, tc_info):
        self.model.tc_info.update(tc_info)
