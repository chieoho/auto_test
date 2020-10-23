# -*- coding: utf-8 -*-
"""
@file: test_tc_repo.py
@desc:
@author: Jaden Wu
@time: 2020/10/23 16:17
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from auto_test.adapters.sql.tc_repo import TCRepoImp, Base


def test_sql_save():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session_obj = scoped_session(session_factory)
    tc_repo = TCRepoImp(session_obj())
    tc_id = tc_repo.save({'priority': 3})
    assert tc_id == 1
