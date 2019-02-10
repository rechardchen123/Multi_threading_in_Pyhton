#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2/10/2019 3:13 PM 
# @Author : Xiang Chen (Richard)
# @File : multiprocessing_exchange.py 
# @Software: PyCharm
import multiprocessing
import time
import random


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('process producer: item %d appended to queue %s' % (item, self.name))
            time.sleep(1)
            print('The size of queue is %s' % self.queue.qsize())


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print('The queue is empty.')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Process consumer: item %d popped from by %s \n' % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()