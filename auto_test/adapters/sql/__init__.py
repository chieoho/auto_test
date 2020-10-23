# -*- coding: utf-8 -*-
"""
@file: __init__.py.py
@desc:
@author: Jaden Wu
@time: 2020/10/19 14:35
"""
import sqlalchemy


def create_database(url, database, character='utf8mb4'):
    """
    服务启动时，没有db就先创建db
    参考sqlalchemy-utils改写
    https://github.com/kvesteri/sqlalchemy-ms_utils/blob/master/sqlalchemy_utils/functions/database.py
    """
    engine = sqlalchemy.create_engine(url)
    if 'sqlite:' in url:
        return
    text = ("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA "
            "WHERE SCHEMA_NAME = '{}'".format(database))
    result_proxy = engine.execute(text)
    result = result_proxy.scalar()
    result_proxy.close()
    database_exists = bool(result)
    if not database_exists:
        result_proxy = engine.execute("CREATE DATABASE {0} CHARACTER SET = '{1}'".format(database, character))
        result_proxy.close()
    engine.dispose()
