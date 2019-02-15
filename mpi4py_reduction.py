#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/15/2019 3:52 PM 
# @Author : Xiang Chen (Richard)
# @File : mpi4py_reduction.py 
# @Software: PyCharm
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
array_size = 3
recvdata = np.zeros(array_size, dtype=np.int)
senddata = (rank + 1) * np.arange(size, dtype=np.int)
print("process %s sending %s " % (rank, senddata))
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
print('on task', rank, 'after Reduce: data = ', recvdata)
