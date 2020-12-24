import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]
def loop(nloop, nsec, lock):
    logging.info("start loop at " + str(nloop) + ctime())
    sleep(nsec)
    logging.info("end loop at " + str(nloop) + ctime())
    lock.release()

# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass


    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    # sleep(6)  # 设置等6秒，由于_thread 规定，主线程退出，强制所有子线程退出
    # loop0()
    # loop1()
    logging.info("end all at " + ctime())


# 如果函数运行的名称等于main
if __name__ == '__main__':
    main()