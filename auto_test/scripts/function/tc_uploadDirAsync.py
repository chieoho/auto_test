# -*- coding: utf-8 -*-
"""
@file: tc_uploadDirAsync.py
@desc:
@author: Jaden Wu
@time: 2020/9/25 10:28
"""
from auto_test.test_case.entity import TCEntity
from auto_test.test_tools.base.local_executor import LocalWithWinpty as Local


class TestCase(TCEntity):
    """
    用例：异步上传目录
    """
    def __init__(self):
        super().__init__()

    def precondition(self):
        return True

    def body(self):
        local = Local()
        w1 = ('请输入指令', r'uploadDirAsync:D:\mc-data\4,/dir50')
        w2 = ('null', 'Ctrl-C')
        _, outs = local.run(r'java -jar D:\mcs\agent\mc-agent-0.0.1-SNAPSHOT.jar', watchers=[w1, w2])
        print(outs)
        if ('Success' in outs) or ('ok' in outs):
            return True
        else:
            return False

    def restore_env(self):
        return True


if __name__ == '__main__':
    tc = TestCase()
    tc_result, _ = tc.run()
    test_case_name = __file__.split('/')[-1][:-len('.py')]
    if tc_result is True:
        print(f'用例{test_case_name}执行成功')
    else:
        print(f'用例{test_case_name}执行失败')
