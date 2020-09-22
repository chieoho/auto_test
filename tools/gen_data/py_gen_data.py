# -*- coding: utf-8 -*-
"""
@file: py_gen_data.py
@desc:
@author: Jaden Wu
@time: 2020/9/22 11:41
"""
from tools.gen_data._interface import GenData


class PyGenData(GenData):
    def __init__(self):
        pass

    def gen_data(self) -> bool:
        print('python gen data')
        return True


if __name__ == '__main__':
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='192.168.66.30', port=22, username='root', password='root')
    stdin, stdout, stderr = client.exec_command('df -h ')
    print(stdout.read().decode('utf-8'))
    client.close()
