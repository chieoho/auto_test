# -*- coding: utf-8 -*-
"""
@file: main.py
@desc:
@author: Jaden Wu
@time: 2020/9/28 10:47
"""
from auto_test.infrastructures.hm_interfaces.console import Console as Controller


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()
