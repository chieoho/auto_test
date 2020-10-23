# -*- coding: utf-8 -*-
"""
@file: interaction.py
@desc:
@author: Jaden Wu
@time: 2020/10/22 16:29
"""
import os
import importlib.util
import inspect
from typing import Tuple
from auto_test.adapters.interfaces.tcs_if import TCSBase
from auto_test.use_cases.interfaces.input_port_if import TCAppIf


class TCInteraction(object):
    """
    testcase interaction
    """
    def __init__(self, tc_app: TCAppIf):
        self.tc_app = tc_app

    @staticmethod
    def _tcs_path_to_tc_parts(tcs_abs_path: str) -> Tuple[callable, callable, callable]:
        module_name = os.path.split(tcs_abs_path)[-1][:-len('.py')]
        spec = importlib.util.spec_from_file_location(
            module_name,
            tcs_abs_path)
        tcs_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tcs_module)
        find_tcs_class = inspect.getmembers(
            tcs_module,
            lambda c:
            inspect.isclass(c) and
            issubclass(c, TCSBase) and
            (c != TCSBase))
        if find_tcs_class:
            tcs_class: TCSBase = find_tcs_class[0][1]
            return tcs_class.precondition, tcs_class.body, tcs_class.restore_env

    def add_tc(self, tc_info_in: dict) -> bool:
        add_res = False
        tcs_path = tc_info_in.get('tcs_path')
        if tcs_path:
            tcs_abs_path = os.path.abspath(tcs_path)
            tc_parts = self._tcs_path_to_tc_parts(tcs_abs_path)
            if tc_parts:
                precondition, body, restore_env = tc_parts
                add_res = self.tc_app.add_testcase(precondition, body, restore_env, tc_info_in)
        return add_res
