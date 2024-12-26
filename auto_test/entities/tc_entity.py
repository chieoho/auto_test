# -*- coding: utf-8 -*-
"""
@file: tc_adapter_if.py
@desc:
@author: Jaden Wu
@time: 2020/10/12 9:37
"""
from dataclasses import dataclass
from enum import Enum


@dataclass
class TCSEntity(object):
    """
    testcase script entity
    """
    precondition: callable = lambda: False
    body: callable = lambda: False
    restore_env: callable = lambda: False
    prepare_res: bool = False
    tcs_run_res: bool = False
    restore_env_res: bool = False

    def run(self):
        """
        运行脚本
        :return:
        """
        self.prepare_res = self.precondition()
        self.tcs_run_res = self.prepare_res and self.body()
        self.restore_env_res = self.restore_env()


class TCResult(Enum):
    """
    testcase result
    """
    unmarked = '未标记'
    passed = '通过'
    failed = '未通过'


@dataclass
class TCEntity(object):
    """
    testcase entity
    """
    case_script: TCSEntity = TCSEntity()
    test_products: str = ''
    priority: int = 3
    case_title: str = ''
    test_steps: str = ''
    case_type: str = ''
    creator: str = ''
    executor: str = ''
    execute_time: str = ''
    result: TCResult = TCResult.unmarked
    status: str = ''
    extension: dict = None

    def execute(self):
        """
        执行用例
        :return:
        """
        self.case_script.run()
        tcs_res = self.case_script.tcs_run_res
        self.result = TCResult.passed if tcs_res else TCResult.failed
