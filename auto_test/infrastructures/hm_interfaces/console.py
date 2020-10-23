# -*- coding: utf-8 -*-
"""
@file: console.py
@desc:
@author: Jaden Wu
@time: 2020/10/19 16:04
"""
import re
from auto_test.use_cases.tc_app import TCApp
from auto_test.adapters.sql.tc_repo import TCRepoImp
from auto_test.adapters.interaction import TCInteraction
from auto_test.infrastructures.databases import init_db


class Console(object):
    """
    命令列表：
    add_tc 添加测试用例
    exe_tc 执行用例

    exit或quit 退出
    """
    def __init__(self):
        self.tc_interaction = TCInteraction(TCApp(TCRepoImp(init_db())))

    @staticmethod
    def test(*args):
        print(args)

    def add_tc(self):
        tcs_relative_path = input('用例脚本路径：')
        tc_info = {
            'tcs_path': tcs_relative_path
        }
        add_res = self.tc_interaction.add_tc(tc_info)
        if add_res is True:
            print('添加用例成功')
        else:
            print('添加用例失败')

    def help(self):
        print(self.__doc__)

    def run(self):
        self.help()
        while 1:
            cmds = input('auto_test >')
            cmd_list = re.split(r'\s+', cmds)
            cmd = cmd_list[0]
            if cmd in ('exit', 'quit'):
                break
            elif cmd == '':
                continue
            elif hasattr(self, cmd):
                getattr(self, cmd)(*cmd_list[1:])
            else:
                print('unknown command')
