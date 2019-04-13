import multiprocessing
from multiprocessing import Process, Pipe
import time


def kirim(keneksi):
    a=[2,4,6]
    keneksi.send(a)
    print("nilai yang di kirim: " ,a)
    keneksi.close()

def kirimb(keneksi):
    b=55
    keneksi.send(b)
    print("nilai : " ,b)
    keneksi.close()

def kirimc(keneksi):
    c = 26
    keneksi.send(c)
    print("nilai : ", c)
    keneksi.close()

def terima (keneksi):
    a1=keneksi.recv()
    time.sleep(1)
    b1=keneksi.recv()
    time.sleep(1)
    c1=keneksi.recv()
    time.sleep(1)
    for i in range(len(a1)):
        if (a1[i] % 2 == 0):
            print("nilai yang di terima: ", a1,b1,c1)
            keneksi.close()
        


if __name__ == '__main__':
    PipaIN, PipaOut = Pipe()
    ProsesKirim=Process(target=kirim,args=(PipaIN,))
    ProsesKirimb = Process(target=kirimb, args=(PipaIN,))
    ProsesKirimc = Process(target=kirimc, args=(PipaIN,))
    ProsesTerima=Process(target=terima,args=(PipaOut,))
    ProsesKirim.start()
    ProsesKirimb.start()
    ProsesKirimc.start()
    ProsesTerima.start()
    ProsesKirim.join()
    ProsesKirimb.join()
    ProsesKirimc.join()
    ProsesTerima.join()
