import multiprocessing
import time



def genap11():
    for i in range(11,21,1):
        if (i % 2 == 0):
            print ('Proses1.a : ',i)
            time.sleep(1)

def genappr():
    for j in range (1,11,1):
        if (j % 2 == 0):
            print('Proses1.b  : ', j)
            time.sleep(1.2)

def ganjil():
    for k in range (50,60,1):
        if (k % 2 == 1):
            print('Proses1.c   : ', k)
            time.sleep(1.4)

def random():
    import random
    for l in range (5):
        print ('Proses1.d    : ', random.randrange(100,200))
        time.sleep(1.6)


if __name__ == '__main__':
        wk1 = multiprocessing.Process(target=genap11)
        wk2 = multiprocessing.Process(target=genappr)
        wk3 = multiprocessing.Process(target=ganjil)
        wk4 = multiprocessing.Process(target=random)

        wk1.start()
        wk2.start()
        wk3.start()
        wk4.start()

        wk1.join()
        wk2.join()
        wk3.join()
        wk4.join()