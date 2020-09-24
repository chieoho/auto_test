# -*- coding: utf-8 -*-
"""
@file: test_exec_by_fabric.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 14:33
"""
from auto_test.test_tools.utils.exec_by_fabric import ExecutorWithFabric


def test_exec_by_fabric_local():
    executor = ExecutorWithFabric()
    ok, out = executor.local('dir')
    assert ok is True
    assert '驱动器' in out

    ok, out = executor.local('tasklist')
    assert ok is True
    assert '映像名称' in out

    ok, out = executor.local('notexistcmd')
    assert ok is False


def test_exec_by_fabric_run():
    executor = ExecutorWithFabric()
    executor.connect('192.168.66.30', user='root', password='root')
    ok, out = executor.run('df -h')
    assert ok is True
    assert '容量' in out

    ok, out = executor.run('date')
    assert ok is True
    assert '星期' in out

    ok, out = executor.run('notexistcmd')
    assert ok is False

    executor.close()
