# -*- coding: utf-8 -*-
"""
@file: local_executor.py
@desc:
@author: Jaden Wu
@time: 2020/9/27 9:19
"""
import re
from winpty import PtyProcess
from auto_test.test_tools.base._interface import LocalExecutor


class LocalWithWinpty(LocalExecutor):
    def __init__(self):
        self.proc = None
        super().__init__()

    def run(self, cmd: str, watchers=None, echo=False) -> tuple:
        if cmd == '':
            return True, ''
        ok, all_outs = False, ''
        try:
            self.proc = PtyProcess.spawn('cmd /c ' + cmd)
            while self.proc.isalive():
                outs = self.proc.read()
                if outs:
                    all_outs += outs
                    if echo:
                        print(outs, end='')
                    if watchers:
                        for pattern, ins in watchers:
                            if re.findall(pattern, outs):
                                if ins == 'Ctrl-C':
                                    self.proc.sendintr()
                                else:
                                    self.proc.write(ins+'\r\n')
                                break
            ok = True if self.proc.exitstatus == 0 else False
        except Exception as run_err:
            print(run_err)
            ok = False
        finally:
            if self.proc:
                self.proc.close()
                del self.proc
        return ok, all_outs


if __name__ == '__main__':
    executor = LocalWithWinpty()
    w1 = ('6379', 'Ctrl-C')
    ok_, outs_ = executor.run('redis-cli', watchers=[w1])
    print(ok_, outs_)
