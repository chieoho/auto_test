# -*- coding: utf-8 -*-
"""
@file: run_cases.py
@desc:
@author: Jaden Wu
@time: 2020/9/28 10:47
"""
import glob
import os
import importlib


def main():
    tc_script_list = glob.iglob(r'.\auto_test\scripts\**\tc_*.py', recursive=True)
    for tcs in tc_script_list:
        module_name = tcs[len('.\\'): -len('.py')].replace(os.sep, '.')
        tc_model = importlib.import_module(module_name)
        if hasattr(tc_model, 'TestCase'):
            tc = tc_model.TestCase()
            tc_result, restore_env_res = tc.run()
            test_case_name = module_name.split('.')[-1]
            if tc_result is True:
                print(f'用例{test_case_name}执行成功')
            else:
                print(f'用例{test_case_name}执行失败')
            if restore_env_res is False:
                print(f'用例{test_case_name}恢复环境失败，连跑终止。')
                break


if __name__ == '__main__':
    main()
