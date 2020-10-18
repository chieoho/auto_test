# -*- coding: utf-8 -*-
"""
@file: test_tc_adapter.py
@desc:
@author: Jaden Wu
@time: 2020/10/16 17:06
"""
from auto_test.entities.tc_entity import TCEntity, TCSEntity
from auto_test.adapters.tc_adapter import TCAdapterImp, TCRepo

repo = {
    1: {'tcs_relative_path': r'..\infrastructures\testcase_scripts\tc_for_unittest_001.py'}
}


class TCRepoImp(TCRepo):
    def get(self, tc_id: int) -> dict:
        tc_in_repo = repo.get(tc_id)
        return tc_in_repo

    def save(self, testcase: dict) -> int:
        tc_id = len(repo) + 1
        repo.update({tc_id: testcase})
        return tc_id

    def update(self, tc_id: int, tc_info: dict) -> bool:
        return True

    def delete(self, tc_id: int) -> bool:
        return True


tc_adapter = TCAdapterImp(TCRepoImp())


testcase_script = TCSEntity(
    precondition=lambda: True,
    body=lambda: True,
    restore_env=lambda: True
)
testcase_ = TCEntity(testcase_script)


def test_adapter_get():
    tc = tc_adapter.get(1)
    assert tc.priority == 3


def test_adapter_save():
    tc_id = tc_adapter.save(testcase_)
    assert isinstance(tc_id, int)
    testcase_get = tc_adapter.get(tc_id)
    assert testcase_get == testcase_


if __name__ == '__main__':
    import importlib.util
    import inspect
    import os
    tcs_relative_path_ = r'..\infrastructures\testcase_scripts\tc_for_unittest_001.py'
    spec = importlib.util.spec_from_file_location(
        "tc_for_unittest_001",
        os.path.abspath(tcs_relative_path_))
    tcs_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tcs_module)
    find_tcs_class = inspect.getmembers(tcs_module, inspect.isclass)
    print(tcs_module.__file__)
