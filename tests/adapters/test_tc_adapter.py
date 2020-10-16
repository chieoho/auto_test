# -*- coding: utf-8 -*-
"""
@file: test_tc_adapter.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 17:06
"""
from auto_test.adapters.tc_adapter import TCAdapterImp, TCRepo


class TCRepoImp(TCRepo):
    def get(self, tc_id: int) -> dict:
        pass

    def save(self, testcase: dict) -> bool:
        pass

    def update(self, tc_id: int, tc_info: dict) -> bool:
        pass

    def delete(self, tc_id: int) -> bool:
        pass


tc_adapter = (TCAdapterImp(TCRepoImp()))


def test_get():
    pass
