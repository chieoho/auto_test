# -*- coding: utf-8 -*-
"""
@file: test_tc_entity.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 10:34
"""
from auto_test.entities.tc_entity import TCSEntity, TCEntity, TCResult


def test_tcs_entity():
    def precondition():
        return True

    def body():
        return True

    def restore_env():
        return True
    testcase_script = TCSEntity(precondition, body, restore_env)
    testcase_script.run()
    assert testcase_script.prepare_res is True
    assert testcase_script.tcs_run_res is True
    assert testcase_script.restore_env_res is True


def test_tc_entity():
    def precondition():
        return True

    def body():
        return True

    def restore_env():
        return True
    testcase_script = TCSEntity(precondition, body, restore_env)
    testcase = TCEntity(testcase_script)
    testcase.execute()
    assert testcase.result == TCResult.passed
