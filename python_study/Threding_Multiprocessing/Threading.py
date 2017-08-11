#! /usr/bin/env python

# bad dummy_threading !!!


import dummy_threading as threading
import time


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# if __name__ == '__main__':
#
#     print('thread %s is running...' % threading.current_thread().name)
#     t = threading.Thread(target=loop, name='LoopThread')
#     t.start()
#     t.join()
#     print('thread %s ended.' % threading.current_thread().name)

def testa():
    time.sleep(3)
    print("a")


def testb():
    time.sleep(3)
    print("b")


ta = threading.Thread(target=testa)
tb = threading.Thread(target=testb)
for t in [ta, tb]:
    t.start()
# for t in [ta, tb]:
#     t.join()
print("DONE")
