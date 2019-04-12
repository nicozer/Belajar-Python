import multiprocessing
import time
from random import randint
import random


def ganjil():
   i = 0
   while i <= 10:
        if (i % 2 == 1):
                print('proses-1..:', i)
                time.sleep(2)
        i += 1


def genap():
    j = 51
    while j <= 60:
        if (j % 2 == 0):
                print('Proses-2....:', j)
                time.sleep(2.2)
        j += 1


def acak():
    k = 1
    while k <= 5:
        print('Proses-3........:', random.randrange(100, 500))
        time.sleep(2.4)
        k += 1


if __name__ == '__main__':
    worker1 = multiprocessing.Process(target=ganjil)
    worker2 = multiprocessing.Process(target=genap)
    worker3 = multiprocessing.Process(target=acak)
    worker1.start()
    worker2.start()
    worker3.start()
    worker1.join()
    worker2.join()
    worker3.join()