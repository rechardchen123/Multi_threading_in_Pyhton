#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 2:11 PM 
# @Author : Xiang Chen (Richard)
# @File : multiprocessing.py 
# @Software: PyCharm
import multiprocessing


def foo(i):
    print('called function in process: %s' % i)
    return


if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
