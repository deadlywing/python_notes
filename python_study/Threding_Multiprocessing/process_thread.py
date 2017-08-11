#! /usr/bin/env python

# condition I

'''
import time

try:
    import threading
except ImportError:
    import dummy_threading as threading


def foo(num):
    time.sleep(2)
    print('thread-{} is now running'.format(num))

for i in range(5):
    t = threading.Thread(target=foo, args=(i,), name='thread-{}'.format(i))
    t.start()

print('-'*10)
print('the end ')
'''

# condition II : join method

'''
import time

try:
    import threading
except ImportError:
    import dummy_threading as threading

def foo(num):
    time.sleep(2)
    print('thread-{} is now running'.format(num))

for i in range(5):
    t = threading.Thread(target=foo, args=(i,), name='thread-{}'.format(i))
    t.start()
    
# DIFFERENT PART !!!!
for i in range(5):
    t.join()

print('-'*10)
print('the end ')
'''

# condition III : LOCK

'''
import time

try:
    import threading
except ImportError:
    import dummy_threading as threading

num = 0
lock = threading.Lock()


def run(k):


    # what will happen if the statement lock.release() occurs in different places?

    
    time.sleep(2)
    lock.acquire()
    global num
    num += 1
    lock.release()
    # time.sleep(0.01)   # this sleep is essential and interesting !!!
    print('the current thread is num({}),the number is now {}'.format(k, num))


for i in range(10):
    t = threading.Thread(target=run, name='thread - {}'.format(i), args=(i,))
    t.start()

'''

# condition IV : Consumer And Producer Model (use queue.Queue)

'''
import time
import queue
import random

try:
    import threading
except ImportError:
    import dummy_threading as threading


def Producer(name, que):
    while True:
        que.put('baozi')
        print('{} Made a baozi...'.format(name))
        time.sleep(random.randrange(5))


def Consumer(name, que):
    while True:
        try:
            # get method will block , compare with get_nowait()
            # que.get()
            que.get_nowait()
            print('{} Got a baozi...'.format(name))
            time.sleep(random.randrange(3))
        except Exception:
            print('no baozi')
            time.sleep(random.randrange(3))


q = queue.Queue()
p1 = threading.Thread(target=Producer, args=('chef1', q))
p2 = threading.Thread(target=Producer, args=('chef2', q))
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer, args=('chenchao', q))
c2 = threading.Thread(target=Consumer, args=('liwang', q))
c1.start()
c2.start()

'''

# conditon V : Consumer And Producer Model (use queue.Queue) with OPP

'''

import time
import queue

try:
    import threading
except ImportError:
    import dummy_threading as threading


class Producer(threading.Thread):
    def __init__(self, name, que):
        self.__name = name
        self.__que = que
        super(Producer, self).__init__()

    def run(self):
        while True:
            if self.__que.full():
                print('baozi is full')
                time.sleep(1)
            else:
                self.__que.put('baozi')
                time.sleep(1)
                print('{} produce a baozi..'.format(self.__name))


class Consumer(threading.Thread):
    def __init__(self, name, que):
        self.__name = name
        self.__que = que
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__que.empty():
                print('bao zi is none')
                time.sleep(1)
            else:
                self.__que.get('baozi')
                time.sleep(1)
                print('{} consume a baozi..'.format(self.__name))


q = queue.Queue(maxsize=100)

for i in range(3):
    name = 'produce-{}'.format(i)
    pro = Producer(name, q)
    pro.start()

for i in range(10):
    name = 'consumer-{}'.format(i)
    con = Consumer(name, q)
    con.start()

'''

# conditon VI : multiprocessing and threading (apply_async() need get() method to get the data)

import os
import multiprocessing
import time

try:
    import threading
except ImportError:
    import dummy_threading


def t_func(n):
    print('thread:{0}  --> {1}'.format(os.getpid(), n))


def f():
    time.sleep(2)
    for i in range(5):
        t = threading.Thread(target=t_func, args=(i,))
        t.start()


pool = multiprocessing.Pool()
res_list = []
for i in range(8):
    res = pool.apply_async(f)
    print('----:', i)
    res_list.append(res)

for r in res_list:
    print(r.get())
