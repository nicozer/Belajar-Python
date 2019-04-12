from multiprocessing import Process,Pipe
import random
import time

def command(p1,p2,p3,p4):
    if p1 < p2 and p1 < p3 and p1 < p4 :
        return print('Rem mobil sekarang !') 
    elif p2 < p1 and p2 < p3 and p2 < p4 :
        return print('Rem mobil sekarang !')
    elif p3 < p1 and p3 < p2 and p3 < p4 :
        return print('Belok kanan sekarang !')
    elif p4 < p1 and p4 < p2 and p4 < p3 :
        return print('Belok kanan sekarang !')

def SensorDepan(depan):
    Jdepan = random.randrange(1,100)
    depan.send(Jdepan)
    print('Jarak depan mobil : ',Jdepan,' cm')
    depan.close()

def SensorBelakang(belakang):
    Jbelakang = random.randrange(1,100)
    belakang.send(Jbelakang)
    print('Jarak belakang mobil : ',Jbelakang,' cm')
    belakang.close()

def SensorKiri(kiri):
    Jkiri = random.randrange(1,100)
    kiri.send(Jkiri)
    print('Jarak kiri mobil : ',Jkiri,' cm')
    kiri.close()

def SensorKanan(kanan):
    Jkanan = random.randrange(1,100)
    kanan.send(Jkanan)
    print('Jarak kanan mobil : ',Jkanan,' cm')
    kanan.close()

def TerimaSensor(depan,belakang,kiri,kanan):
    DP = depan.recv()
    BK = belakang.recv()
    KI = kiri.recv()
    KA = kanan.recv()
    
    print('--- Tindakan ---')
    command(DP,BK,KI,KA)

if __name__ == '__main__':
    depanIn,depanOut = Pipe()
    belakangIn,belakangOut = Pipe()
    kiriIn,kiriOut = Pipe()
    kananIn,kananOut = Pipe()
    
    KirimSensorDepan = Process(target=SensorDepan,args=(depanIn,))
    KirimSensorBelakang = Process(target=SensorBelakang,args=(belakangIn,))
    KirimSensorKiri = Process(target=SensorKiri,args=(kiriIn,))
    KirimSensorKanan = Process(target=SensorKanan,args=(kananIn,))
    TerimaSensorSemua = Process(target=TerimaSensor,args=(depanOut,belakangOut,kiriOut,kananOut))

    KirimSensorDepan.start()
    KirimSensorBelakang.start()
    KirimSensorKiri.start()
    KirimSensorKanan.start()
    TerimaSensorSemua.start()

    KirimSensorDepan.join()
    KirimSensorBelakang.join()
    KirimSensorKiri.join()
    KirimSensorKanan.join()
    TerimaSensorSemua.join()