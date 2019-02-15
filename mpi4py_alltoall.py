#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/15/2019 3:46 PM 
# @Author : Xiang Chen (Richard)
# @File : mpi4py_alltoall.py 
# @Software: PyCharm
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
a_size = 1

senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size * a_size, dtype=int)

comm.Alltoall(senddata, recvdata)
print(" process %s sending %s receiving %s" % (rank, senddata, recvdata))
