#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/15/2019 3:41 PM 
# @Author : Xiang Chen (Richard)
# @File : mpi4py_gather.py 
# @Software: PyCharm
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank + 1) ** 2
data = comm.gather(data, root=0)
if rank == 0:
    print("rank = %s" % rank + "... receiving data to other process.")
    for i in range(1, size):
        data[i] = (i + 1) ** 2
        value = data[i]
        print(" process %s receiving %s from process %s" % (rank, value, i))
