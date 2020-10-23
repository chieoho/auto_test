# -*- coding: utf-8 -*-
"""
@file: test_interaction.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 17:06
"""
import os
from auto_test.adapters.interaction import TCInteraction, TCAppIf

tc_info_test = {
    'tcs_path': os.path.abspath(__file__ + '/../../infrastructures/testcase_scripts/tc_for_unittest_001.py')
}


class TCApp(TCAppIf):
    def add_testcase(
            self,
            precondition: callable,
            body: callable,
            restore_env: callable,
            tc_info_in: dict
    ) -> bool:
        return True


tc_interaction = TCInteraction(TCApp())


def test_tcs_path_to_tc_parts():
    tcs_abs_path = tc_info_test.get('tcs_path')
    precondition, body, restore_env = tc_interaction._tcs_path_to_tc_parts(tcs_abs_path)
    assert callable(precondition) is True
    assert callable(body) is True
    assert callable(restore_env) is True


def test_add_tc():
    add_res = tc_interaction.add_tc(tc_info_test)
    assert add_res is True


if __name__ == '__main__':
    print(__file__)
    print(os.path.abspath(__file__ + '/../../infrastructures'))
    print(tc_info_test.get('tcs_path'))
