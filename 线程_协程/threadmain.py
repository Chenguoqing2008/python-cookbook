#! /usr/bin/python
import threading


def do_something():

    global x, lock
    lock = threading.Lock()

    # x = 0
    # print('thread 2 is there.')
    # while not terminate:
    #     x += 1
    #     pass
    # print(x)
    lock.acquire()
    while x < 300:
        x += 1
    print(x)
    lock.release()


def do_another():
    global x, lock
    lock = threading.Lock()

    lock.acquire()
    while x < 600:
        x += 1
    print(x)
    lock.release()


def main():
    global x, lock
    x = 0
    lock = threading.Lock()

    # terminate = False

    t = threading.Thread(target=do_something)
    t.start()
    t.join()
    print(t.ident)

    t1 = threading.Thread(target=do_another)
    t1.start()
    t1.join()
    print(t1.ident)
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    #
    # print(t.is_alive())
    # input('Terminate the process')
    # terminate = True
    # input('the thread has terminated, wait a second.')
    #
    # print(t.is_alive())


if __name__ == '__main__':
    main()
