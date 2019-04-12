import time
import multiprocessing
import random


def kuadrat():
    for i in range (1,11,1):
        print('Bilangan Asli--: ',i)
        time.sleep(1)
        print('Bilangan Kuadrat---: ',i**2)
        time.sleep(1.4)


if __name__ == '__main__':
    wk1 = multiprocessing.Process(target=kuadrat)
    wk1.start();
    wk1.join();