# -*- coding: utf-8 -*-
"""
@file: local_executor.py
@desc:
@author: Jaden Wu
@time: 2020/9/27 9:19
"""
import re
from winpty import PtyProcess
from auto_test.test_tools.utils._interface import LocalExecutor


class LocalWithWinpty(LocalExecutor):
    def __init__(self):
        super().__init__()

    def run(self, cmd: str, watchers=None) -> tuple:
        if cmd == '':
            return True, ''
        ok, all_outs = False, ''
        try:
            proc = PtyProcess.spawn('cmd /c ' + cmd)
            while proc.isalive():
                outs = proc.read()
                if outs:
                    all_outs += outs
                    # print(outs, end='')
                    if watchers:
                        for pattern, ins in watchers:
                            if re.findall(pattern, outs):
                                if ins == 'Ctrl-C':
                                    proc.sendintr()
                                else:
                                    proc.write(ins+'\r\n')
                                break
            ok = True if proc.exitstatus == 0 else False
        except Exception as run_err:
            print(run_err)
            ok = False
        finally:
            proc.close()
            del proc
        return ok, all_outs


if __name__ == '__main__':
    executor = LocalWithWinpty()
    w1 = ('6379', 'Ctrl-C')
    ok_, outs_ = executor.run('redis-cli', watchers=[w1])
    print(ok_, outs_)
