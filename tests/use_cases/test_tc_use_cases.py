# -*- coding: utf-8 -*-
"""
@file: test_tc_use_cases.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 15:27
"""
from auto_test.use_cases.tc_use_cases import TCApp, TCAdapter, TCEntity, TCResult
from auto_test.entities.tc_entity import TCSEntity

testcase_script = TCSEntity(
    precondition=lambda: True,
    body=lambda: True,
    restore_env=lambda: True
)
testcase_ = TCEntity(testcase_script)


class TCAdapterImp(TCAdapter):
    def get(self, case_id: int) -> TCEntity:
        return testcase_

    def save(self, testcase: TCEntity) -> bool:
        return True

    def mark(self, case_id: int) -> bool:
        return True

    def delete(self, case_id: int) -> bool:
        return True


def test_testcase_app():
    tc_app = TCApp(TCAdapterImp())
    assert tc_app.add_testcase(testcase_) is True
    assert tc_app.view_testcase(1) == testcase_
    assert tc_app.execute_testcase(1) == TCResult.passed
    assert tc_app.mark_testcase(1) is True
    assert tc_app.delete_testcase(1) is True
