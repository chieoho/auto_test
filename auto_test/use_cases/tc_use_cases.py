# -*- coding: utf-8 -*-
"""
@file: tc_use_cases.py
@desc: 测试用例的用例（应用场景）
@author: Jaden Wu
@time: 2020/10/14 9:57
"""
from auto_test.entities.tc_entity import TCEntity, TCResult
from auto_test.use_cases.interfaces.tc_adapter_if import TCAdapter


class TCApp(object):
    """
    testcase use_cases
    """
    def __init__(self, testcase_adapter: TCAdapter):
        self.testcase_adapter = testcase_adapter

    def add_testcase(self, testcase_info: TCEntity) -> bool:
        save_res = self.testcase_adapter.save(testcase_info)
        return save_res

    def view_testcase(self, testcase_id: int) -> TCEntity:
        testcase = self.testcase_adapter.get(testcase_id)
        return testcase

    def execute_testcase(self, testcase_id: int) -> TCResult:
        testcase = self.testcase_adapter.get(testcase_id)
        testcase.execute()
        return testcase.result

    def mark_testcase(self, testcase_id: int) -> bool:
        mark_res = self.testcase_adapter.mark(testcase_id)
        return mark_res

    def delete_testcase(self, testcase_id: int) -> bool:
        del_res = self.testcase_adapter.delete(testcase_id)
        return del_res
