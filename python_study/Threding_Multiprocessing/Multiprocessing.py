#! usr/bin/env python
# act well !!

from multiprocessing import Process, Pool
import time, os


def run_proc(name):
    print('run child process {0} ({1}).'.format(name, os.getpid()))


def count_fun(n):
    time.sleep(2)
    print(n * n)
    return n * n + n ** 2


if __name__ == '__main__':
    # print('parent process {}.'.format(os.getpid()))
    # p = Process(target=run_proc, args=('test',))
    # print('child process will begin...')
    # p.start()
    # p.join()
    # print('child process end...')

    # Pool
    time.sleep(1)
    p = Pool(20)
    p.map(count_fun, range(100))
