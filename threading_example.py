#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 1/26/2019 6:42 PM 
# @Author : Xiang Chen (Richard)
# @File : threading.py 
# @Software: PyCharm
import threading

def function(i):
    print("function called by thread %i\n" %i)
    return

threads=[]
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
