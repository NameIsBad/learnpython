# -*- coding:utf-8 -*-

' a test module '

__author__ = '杜佳迪'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello word！%s' % args[0])
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('To many arguments!')


if __name__ == '__main__':
    test()
