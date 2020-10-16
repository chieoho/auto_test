# -*- coding: utf-8 -*-
"""
@file: main.py
@desc:
@author: Jaden Wu
@time: 2020/9/28 10:47
"""
import glob
import os
import importlib
import inspect
from auto_test.adapters.interfaces.tcs_if import TCSBase


def main():
    tc_script_list = glob.iglob(r'.\auto_test\infrastructures\testcase_scripts\**\tc_*.py', recursive=True)
    for tcs in tc_script_list:
        module_name = tcs[len('.\\'): -len('.py')].replace(os.sep, '.')
        tc_model = importlib.import_module(module_name)
        find_tcs_class = inspect.getmembers(
            tc_model,
            lambda c:
            inspect.isclass(c) and
            issubclass(c, TCSBase) and
            (c != TCSBase))
        if find_tcs_class:
            tcs_class = find_tcs_class[0][1]
            test_case_name = module_name.split('.')[-1]
            print(f'用例{test_case_name}开始运行')
            tc_result, restore_env_res = tcs_class().run()
            if tc_result is True:
                print(f'用例{test_case_name}运行成功')
            else:
                print(f'用例{test_case_name}运行失败')
            if restore_env_res is False:
                print(f'用例{test_case_name}恢复环境失败，连跑终止。')
                break


if __name__ == '__main__':
    main()
