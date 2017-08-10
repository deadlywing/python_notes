#! usr/bin/env python
# bad  !!!!

import dummy_threading as threading
import time

num = 0
lock = threading.Lock()


def run():
    time.sleep(1)
    lock.acquire()
    global num
    num += 1
    lock.release()
    print('{}'.format(num))


for i in range(10):
    t = threading.Thread(target=run)
    t.start()
