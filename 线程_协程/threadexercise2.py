#! /usr/bin/python
# _*_ coding: utf-8 _*_
import threading
import time


def sleeper(n, name):
    print('I am {}  i will sleep 5 seconds'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep'.format(name))


t = threading.Thread(target=sleeper, name='thread 1', args=(5, 'thread 1'))

t.start()
# t.join()

print('hello')
print('hello')



