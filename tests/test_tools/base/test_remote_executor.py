# -*- coding: utf-8 -*-
"""
@file: test_remote_executor.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 14:33
"""
from auto_test.test_tools.base.remote_executor import RemoteWithFabric


def test_remote_with_fabric():
    executor = RemoteWithFabric()
    executor.connect('192.168.66.21', user='root', password='password')

    ok, outs = executor.run('df -h')
    assert ok is True
    assert '容量' in outs

    ok, outs = executor.run('date')
    assert ok is True
    assert '星期' in outs

    ok, outs = executor.run('')
    assert ok is True

    w1 = (r'Enter password:', 'anyun100')
    w2 = (r'MariaDB \[\(none\)\]', 'quit')
    ok, outs = executor.run('mysql -umetadata -p', watchers=[w1, w2])
    assert ok is True
    assert 'Bye' in outs

    ok, outs = executor.run('notexistcmd')
    assert ok is False
