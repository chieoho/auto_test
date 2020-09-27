# -*- coding: utf-8 -*-
"""
@file: sql_executor.py
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

    def connect(self, host: str, user: str, password: str, db=None,
                port=3306, charset='utf8mb4') -> bool:
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
        """
        增，删，改都用此方法
        :param sql:
        :return:
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            self.connection.commit()
        except Exception as exe_err:
            print(exe_err)
            self.connection.rollback()

    def query(self, sql) -> list:
        cursor = self.connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def close(self) -> bool:
        try:
            self.connection.close()
            return True
        except Exception as close_err:
            print(close_err)
            return False
