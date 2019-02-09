#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 1/26/2019 6:53 PM 
# @Author : Xiang Chen (Richard)
# @File : threading_exaple_time.py 
# @Software: PyCharm
import threading
import time

def first_function():
    print(threading.currentThread().getName()+
          str(' is Starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName()+
          str(' is Exising \n'))
    return

def second_function():
    print(threading.currentThread().getName() +
          str(' is Starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName() +
          str(' is Exising \n'))
    return

def third_function():
    print(threading.currentThread().getName() +
          str(' is Starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName() +
          str(' is Exising \n'))
    return

if __name__ == "__main__":
    t1 = threading.Thread(name='first_function',
                          target=first_function)
    t2 = threading.Thread(name='second_function',
                          target=second_function)
    t3 = threading.Thread(target=third_function)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


