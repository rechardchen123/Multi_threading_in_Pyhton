#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 3:41 PM 
# @Author : Xiang Chen (Richard)
# @File : hello_mpi.py 
# @Software: PyCharm
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('hello world from process', rank)
