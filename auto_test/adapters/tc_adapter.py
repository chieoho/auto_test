# -*- coding: utf-8 -*-
"""
@file: tc_adapter.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 10:14
"""
import os
import importlib.util
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

    @staticmethod
    def _tc_path_to_class(tcs_abs_path: str) -> TCSEntity:
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
            tcs_class = find_tcs_class[0][1]
            testcase_script = TCSEntity(
                precondition=tcs_class.precondition,
                body=tcs_class.body,
                restore_env=tcs_class.restore_env
            )
            return testcase_script

    def get(self, tc_id: int) -> TCEntity:
        testcase_in_repo = self.repo.get(tc_id)
        tcs_relative_path = testcase_in_repo.pop('tcs_relative_path', None)
        if tcs_relative_path:
            tcs_abs_path = os.path.abspath(tcs_relative_path)
            testcase_script = self._tc_path_to_class(tcs_abs_path)
            if testcase_script:
                return TCEntity(testcase_script, **testcase_in_repo)

    def save(self, testcase: TCEntity) -> int:
        pass

    def mark(self, case_id: int) -> bool:
        pass

    def delete(self, case_id: int) -> bool:
        pass
