# -*- coding: utf-8 -*-
"""
@file: tc_uploadDirAsync.py
@desc:
@author: Jaden Wu
@time: 2020/9/25 10:28
"""
from auto_test.test_case.entity import TestCase
from auto_test.test_tools.utils.exec_by_fabric import ExecutorWithFabric


class TestCaseScript(TestCase):
    """
    用例：异步上传目录
    """
    def __init__(self):
        super().__init__()

    def precondition(self):
        return True

    def body(self):
        executor = ExecutorWithFabric()
        resp1 = ('请输入指令', r'uploadDirAsync:D:\mc-data\4,/dir50')
        resp2 = ('null', 'taskkill /f /im java.exe')
        ok, out = executor.local(r'java -jar D:\mcs\agent\mc-agent-0.0.1-SNAPSHOT.jar', watchers=[resp1, resp2])
        if ok and ('Success' in out) or ('ok' in out):
            return True
        else:
            return False

    def restore_env(self):
        return True


if __name__ == '__main__':
    tc_script = TestCaseScript()
    tc_result, _ = tc_script.run()
    if tc_result is True:
        print('用例tc_uploadDirAsync执行成功')
    else:
        print('用例tc_uploadDirAsync执行失败')
