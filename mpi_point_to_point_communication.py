#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 3:47 PM 
# @Author : Xiang Chen (Richard)
# @File : mpi_point_to_point_communication.py 
# @Software: PyCharm
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print('my rank is :', rank)

if rank == 0:
    data = 100000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data % s " % data + "to process % d" % destination_process)

if rank == 1:
    destination_process = 8
    comm.send(data, dest=destination_process)
    print("sending data % s :" % data + "to process % d" % destination_process)

if rank == 4:
    data = comm.recv(source=0)
    print("data received is = % s" % data)

if rank == 8:
    data1 = comm.recv(source=1)
    print('data1 receive is = %s ' % data1)
