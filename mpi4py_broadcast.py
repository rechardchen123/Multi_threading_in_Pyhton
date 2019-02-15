#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/15/2019 3:19 PM 
# @Author : Xiang Chen (Richard)
# @File : mpi4py_broadcast.py 
# @Software: PyCharm
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None
variable_to_share = comm.bcast(variable_to_share, root=0)
print('process=%d' % rank + "variable shared = %d" % variable_to_share)
