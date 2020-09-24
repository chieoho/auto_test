# -*- coding: utf-8 -*-
"""
@file: exec_by_pymysql.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 17:10
"""
import pymysql
from auto_test.test_tools.utils._interface import SqlExecutor


class ExeWithPymysql(SqlExecutor):
    def __init__(self):
        self.connection = None
        super().__init__()

    def connect(self, host: str, user: str, password: str, db: str, port=3306, charset='utf8mb4') -> bool:
        try:
            self.connection = pymysql.connect(host=host,
                                              port=port,
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset=charset)
            return True
        except Exception as conn_err:
            print(conn_err)
            return False

    def change(self, sql):
        pass

    def query(self, sql) -> str:
        pass
