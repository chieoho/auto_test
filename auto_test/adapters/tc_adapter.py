# -*- coding: utf-8 -*-
"""
@file: tc_adapter.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 10:14
"""
import os
import importlib
import inspect
from auto_test.entities.tc_entity import TCEntity, TCSEntity
from auto_test.use_cases.interfaces.tc_adapter_if import TCAdapter
from auto_test.adapters.interfaces.repositories_if import TCRepo
from auto_test.adapters.interfaces.tcs_if import TCSBase


class TCAdapterImp(TCAdapter):
    """
    testcase adapter implement
    """
    def __init__(self, repo: TCRepo):
        self.repo = repo

    def get(self, case_id: int) -> TCEntity:
        testcase_in_dict = self.repo.get(case_id)
        case_script_path = testcase_in_dict.pop('case_script_path', None)
        if case_script_path:
            module_name = case_script_path[len('.\\'): -len('.py')].replace(os.sep, '.')
            tcs_module = importlib.import_module(module_name)
            find_tcs_class = inspect.getmembers(
                tcs_module,
                lambda c:
                inspect.isclass(c) and
                issubclass(c, TCSBase) and
                (c != TCSBase))
            if find_tcs_class:
                tcs_class = find_tcs_class[0][1]
                testcase_script = TCSEntity(
                    precondition=tcs_class.precondition,
                    body=tcs_class.body,
                    restore_env=tcs_class.restore_env
                )
                return TCEntity(testcase_script, **testcase_in_dict)

    def save(self, testcase: TCEntity) -> bool:
        pass

    def mark(self, case_id: int) -> bool:
        pass

    def delete(self, case_id: int) -> bool:
        pass
