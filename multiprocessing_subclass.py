#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 3:08 PM 
# @Author : Xiang Chen (Richard)
# @File : multiprocessing_subclass.py 
# @Software: PyCharm
import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print('called run method in process: %s' % self.name)
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()
