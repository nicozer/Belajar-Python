import multiprocessing
from multiprocessing import Process, Pipe

a=10
b=10

def kirim(keneksi):
    a=[15,25,35]
    keneksi.send(a)
    print("nilai yang di kirim: ",a,b)
    keneksi.close()


def terima (keneksi):
    print("nilai yang di terima: ", keneksi.recv(),b)


if __name__ == '__main__':
    PipaIN, PipaOut = Pipe()
    ProsesKirim=Process(target=kirim,args=(PipaIN,))
    ProsesTerima=Process(target=terima,args=(PipaOut,))
    ProsesKirim.start()
    ProsesTerima.start()
    ProsesKirim.join()
    ProsesTerima.join()