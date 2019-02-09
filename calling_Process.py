#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 1/26/2019 6:06 PM 
# @Author : Xiang Chen (Richard)
# @File : calling_Process.py 
# @Software: PyCharm
import os
import sys

program = "Python"
print("Process calling")
arguments = ["called_Process.py"]

os.execvp(program,(program,) +tuple(arguments))
print("Good Bye!!")
