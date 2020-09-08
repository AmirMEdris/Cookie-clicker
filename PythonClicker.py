from pyautogui import moveTo,click
from time import time as t
import threading
import multiprocessing
import cookie


def clickthecookie(times):
   
    moveTo(135, 513)
    for i in range(times):
        click()

def TimeTheClicks(x):
    times = x
    start = t()
    clickthecookie(times)
    finish = t()
    return finish - start
def f(x):
    return (0.1158*x)+0.1128
def timedClickCookie100():
    start=t()
    clickthecookie(100)
    print(f'Finished 100 in {t()-start} seconds')
    return t()-start
def c25threads():
    threads=[]
    for _ in range(10):
        th=threading.Thread(target=cookie.clickthecookie)
        th.start()
        threads.append(th)


def dude():
    ps = []
    for _ in range(10):
        p = multiprocessing.Process(target=cookie.clickthecookie)
        p.start()
        ps.append(p)


# for thread in threads:
#     thread.join()
def bruh():
    threads = []
    for _ in range(10):
        th = threading.Thread(target=c25threads)
        th.start()
        threads.append(th)


