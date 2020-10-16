# -*- coding: utf-8 -*-
"""
@file: tc_upload_001.py
@desc:
@author: Jaden Wu
@time: 2020/9/22 9:49
"""
from auto_test.adapters.interfaces.tcs_if import TCSBase
from auto_test.infrastructures.testcase_scripts.test_tools.gen_data.py_gen_data import PyGenData as GenDate


class TestCase(TCSBase):
    """
    用例：文件上传
    一、前提条件
    1、生成上传用数据
    二、用例主体
    1、
    2、
    三、恢复环境
    1、清除上传过程产生的缓存
    """
    def __init__(self):
        super().__init__()

    def precondition(self):
        print('precondition')
        GenDate().gen_data()
        return True

    def body(self):
        print('body')
        return True

    def restore_env(self):
        print('restore env')
        return True


if __name__ == '__main__':
    tc_script = TestCase()
    result = tc_script.run()
    print(result)
