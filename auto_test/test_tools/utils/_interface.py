# -*- coding: utf-8 -*-
"""
@file: _interface.py
@desc: 工具层与操作系统交互接口
@author: Jaden Wu
@time: 2020/9/24 11:33
"""
from abc import ABCMeta, abstractmethod


class CmdExecutor(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, host: str, port: int, user: str, password: str) -> bool:
        pass

    @abstractmethod
    def run(self, cmd: str) -> tuple:
        pass

    @abstractmethod
    def local(self, cmd: str) -> tuple:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass


class SqlExecutor(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, host: str, user: str, password: str, db: str, port: int, charset: str) -> bool:
        pass

    @abstractmethod
    def change(self, sql) -> bool:
        pass

    @abstractmethod
    def query(self, sql) -> str:
        pass

