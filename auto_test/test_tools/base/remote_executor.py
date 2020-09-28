# -*- coding: utf-8 -*-
"""
@file: remote_executor.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 13:29
"""
from fabric.connection import Connection
from invoke import Responder
from auto_test.test_tools.base._interface import RemoteExecutor


class RemoteWithFabric(RemoteExecutor):
    def __init__(self):
        self.connection = None
        super().__init__()

    def connect(self, host: str, user='root', password='', port=22) -> bool:
        try:
            self.connection = Connection(host, user, port, connect_kwargs={'password': password})
            return True
        except Exception as conn_err:
            print(conn_err)
            return False

    def run(self, cmd: str, watchers=None) -> tuple:
        if watchers is None:
            watchers = []
        else:
            watchers = list(map(lambda w: Responder(w[0], w[1]+'\n'), watchers))
        result = self.connection.run(cmd, warn=True, hide=True, encoding='utf-8', pty=True, watchers=watchers)
        if result.ok:
            return True, result.stdout
        else:
            return False, ''

    def close(self) -> bool:
        try:
            if self.connection:
                self.connection.close()
                return True
        except Exception as close_err:
            print(close_err)
            return False


if __name__ == '__main__':
    executor = RemoteWithFabric()
    executor.connect('192.168.66.21', user='root', password='password')
    w1 = (r'Enter password:', 'anyun100')
    w2 = (r'MariaDB', 'quit')
    ok, out = executor.run('mysql -umetadata -p', watchers=[w1, w2])
    print(out)
    assert ok is True
    assert 'MariaDB [(none)]' in out
