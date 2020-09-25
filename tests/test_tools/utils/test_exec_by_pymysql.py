# -*- coding: utf-8 -*-
"""
@file: test_exec_by_fabric.py
@desc:
@author: Jaden Wu
@time: 2020/9/24 21:39
"""
import sqlite3
from auto_test.test_tools.utils.exec_by_pymysql import ExeWithPymysql


def test_change_and_query():
    sql_executor = ExeWithPymysql()
    sql_executor.connection = sqlite3.connect(':memory:')
    create_table = """create table employee (
         first_name  char(20) not null,
         last_name  char(20),
         age int,  
         sex char(1),
         income float )"""
    insert_sql = """insert into employee(first_name,
         last_name, age, sex, income)
         values ('mac', 'mohan', 20, 'm', 2000)"""
    query_sql = "select * from employee where first_name = 'mac'"
    sql_executor.change(create_table)
    sql_executor.change(insert_sql)
    results = sql_executor.query(query_sql)
    sql_executor.close()
    assert results[0][1] == 'mohan'
