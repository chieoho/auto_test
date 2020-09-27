# -*- coding: utf-8 -*-
"""
@file: tc_uploadDirAsync.py
@desc:
@author: Jaden Wu
@time: 2020/9/25 10:28
"""
from auto_test.test_case.entity import TestCase
from auto_test.test_tools.utils.local_executor import LocalWithWinpty


class TestCaseScript(TestCase):
    """
    用例：异步上传目录
    """
    def __init__(self):
        super().__init__()

    def precondition(self):
        return True

    def body(self):
        executor = LocalWithWinpty()
        w1 = ('请输入指令', r'uploadDirAsync:D:\mc-data\4,/dir50')
        w2 = ('null', 'Ctrl-C')
        ok, outs = executor.run(r'java -jar D:\mcs\agent\mc-agent-0.0.1-SNAPSHOT.jar', watchers=[w1, w2])
        print(ok, outs)
        if ok and ('Success' in outs) or ('ok' in outs):
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
