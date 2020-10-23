# -*- coding: utf-8 -*-
"""
@file: tc_app.py
@desc: 测试用例的用例（应用场景）
@author: Jaden Wu
@time: 2020/10/14 9:57
"""
from auto_test.entities.tc_entity import TCSEntity, TCEntity
from auto_test.use_cases.interfaces.input_port_if import TCAppIf
from auto_test.use_cases.interfaces.output_port_if import TCRepoIf


class TCApp(TCAppIf):
    """
    testcase use_cases
    """
    def __init__(self, tc_repo: TCRepoIf):
        self.tc_repo = tc_repo

    def add_testcase(
            self,
            precondition: callable,
            body: callable,
            restore_env: callable,
            tc_info_in: dict
    ) -> bool:
        tc_script: TCSEntity = TCSEntity(precondition, body, restore_env)
        tcs_path = tc_info_in.pop('tcs_path', None)
        testcase: TCEntity = TCEntity(tc_script, **tc_info_in)
        tc_info_out = {
            'tcs_path': tcs_path,
            'priority': testcase.priority
        }
        tc_id = self.tc_repo.save(tc_info_out)
        return isinstance(tc_id, int)
