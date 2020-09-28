# -*- coding: utf-8 -*-
"""
@file: test_local_executor.py
@desc:
@author: Jaden Wu
@time: 2020/9/27 9:46
"""
from auto_test.test_tools.base.local_executor import LocalWithWinpty


def test_local_with_winpty():
    executor = LocalWithWinpty()

    ok, outs = executor.run('dir')
    assert ok is True
    assert '驱动器' in outs

    ok, outs = executor.run('tasklist')
    assert ok is True
    assert '映像名称' in outs

    w = ('information', 'exit()\n')
    ok, outs = executor.run('python', watchers=[w])
    assert ok is True
    assert 'exit' in outs

    ok, outs = executor.run('')
    assert ok is True

    ok, outs = executor.run('notexistcmd')
    assert ok is False

    w1 = ('6379', 'Ctrl-C')
    ok, outs = executor.run('redis-cli', watchers=[w1])
    assert ok is False
