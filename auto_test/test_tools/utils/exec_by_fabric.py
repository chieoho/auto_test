# -*- coding: utf-8 -*-
"""
@file: exec_by_fabric.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 13:29
"""
import os
from fabric.connection import Connection
from auto_test.test_tools.utils._interface import CmdExecutor


class ExecutorWithFabric(CmdExecutor):
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

    def run(self, cmd: str) -> tuple:
        result = self.connection.run(cmd, warn=True, hide=True, encoding='utf-8')
        if result.ok:
            return True, result.stdout
        else:
            return False, ''

    def local(self, cmd: str) -> tuple:
        conn = Connection('local')
        result = conn.local(cmd, warn=True, hide=True, env=os.environ)
        conn.close()
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
