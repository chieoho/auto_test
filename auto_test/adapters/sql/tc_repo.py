# -*- coding: utf-8 -*-
"""
@file: tc_repo.py
@desc:
@author: Jaden Wu
@time: 2019/7/25 15:22
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PickleType
from auto_test.use_cases.interfaces.output_port_if import TCRepoIf


Base = declarative_base()


class TCModel(Base):
    __tablename__ = 'testcase'
    tc_id = Column(Integer, primary_key=True)
    tcs_path = Column(String(128))
    test_products = Column(String(32))
    priority = Column(Integer)
    case_title = Column(String(64))
    test_steps = Column(String(8192))
    case_type = Column(String(16))
    creator = Column(String(16))
    executor = Column(String(16))
    execute_time = Column(String(32))
    result = Column(Integer)
    status = Column(String(8))
    extension = Column(PickleType)


class TCRepoImp(TCRepoIf):
    def __init__(self, session):
        self.model = TCModel
        self.session = session

    def __del__(self):
        self.session.close()

    def save(self, testcase: dict) -> int:
        new_tc = self.model(**testcase)
        self.session.add(new_tc)
        self.session.commit()
        return new_tc.tc_id


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    engine = create_engine('sqlite:///../../infrastructures/databases/auto_test.db')
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    tc_repo = TCRepoImp(Session())
    print(tc_repo.save({'priority': 3}))
