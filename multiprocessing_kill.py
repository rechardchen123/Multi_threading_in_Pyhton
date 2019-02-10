#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 2:27 PM 
# @Author : Xiang Chen (Richard)
# @File : multiprocessing_kill.py 
# @Software: PyCharm
import multiprocessing
import time

def foo():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')


if __name__=='__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p,p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
