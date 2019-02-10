#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 2:21 PM 
# @Author : Xiang Chen (Richard)
# @File : multiprocessing_background.py 
# @Software: PyCharm
import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s " % name)
    time.sleep(3)
    print("Exiting %s " % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
