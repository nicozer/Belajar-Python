import multiprocessing
from multiprocessing import Process, Pipe
import random


def kanan(koneksi):
        jkanan = random.randrange(1, 2000)
        print("Jarak Kanan Mobil = ", jkanan, "cm")
        koneksi.send(jkanan)
        koneksi.close()


def kiri(koneksi):
        jkiri = random.randrange(1, 2000)
        print("Jarak Kiri Mobil = ", jkiri, "cm")
        koneksi.send(jkiri)
        koneksi.close()


def depan(koneksi):
        jdepan = random.randrange(1, 1000)
        print("Jarak Depan Mobil = ", jdepan, "cm")
        koneksi.send(jdepan)
        koneksi.close()


def belakang(koneksi):
        jbelakang = random.randrange(1, 1000)
        print("Jarak Belakang Mobil = ", jbelakang, "cm")
        koneksi.send(jbelakang)
        koneksi.close()


def MainControl(koneksi):
    BatasKanan=koneksi.recv()
    BatasKiri=koneksi.recv()
    BatasDepan=koneksi.recv()
    BatasBelakang=koneksi.recv()
    print("\n<=== Kondisi Mobil ===>")

    #Mengatur Sistem jika salah satu jarak 0
    if (BatasKanan == 0 & BatasKiri == 0 & BatasDepan == 0 & BatasBelakang == 0):
        print("MOBIL TERTABRAK!!!!!")

    #Mengatur Sistem jika bagian kiri dan kanan mobil terlalu mepet
    elif ((BatasKiri <= 40) & (BatasKanan <= 40)):
        print("Hati Hati Bagian Kiri dan Kanan anda Kurang Dari 40cm")
        print("\n<===     Solusi    ===>")
        print("JAGA KECEPATAN & JARAK!!!")

    #Mengatur Sistem jika bagian Depan dan Belakang mobil terlalu mepet
    elif ((BatasDepan <= 40) & (BatasBelakang <= 40)):
        print("Hati Hati Bagian Depan dan Belakang anda Kurang Dari 40cm")
        print("\n<===     Solusi    ===>")
        print("JAGA KECEPATAN & JARAK!!!")

    #Mengatur Sistem jika bagian Kanan,Kiri,Depan,dan Belakang mobil terlalu mepet
    elif((BatasKiri <= 40) & (BatasKanan <= 40) & (BatasDepan <= 40) & (BatasBelakang <= 40)):
        print("Hati Hati Semua Bagian Mobil Kurang Dari 40cm")
        print("\n<===     Solusi    ===>")
        print("JAGA KECEPATAN & JARAK!!!")

    #Mengatur Sistem jika Bagian Kanan terlalu mepet
    elif (BatasKanan <= 40):
        print("Jarak Bagian Kanan Mobil Kurang Dari 40cm")
        print("\n<===     Solusi    ===>")
        print("TOLONG BELOK KE KIRI!!!")

    #Mengatur Sistem jika Bagian Kiri terlalu mepet
    elif (BatasKiri <= 40):
        print("Jarak Bagian Kiri Mobil Kurang Dari 40cm")
        print("\n<===     Solusi    ===>")
        print("TOLONG BELOK KE KANAN!!!")

    #Mengatur Sistem jika Bagian Depan terlalu mepet
    elif (BatasDepan <= 200):
        print("Jarak Bagian Depan Mobil Kurang Dari 2m")
        print("\n<===     Solusi    ===>")
        print("REM MOBIL SEGERA!!!")

    #Mengatur Sistem jika Bagian Belakang terlalu mepet
    elif (BatasBelakang <= 200):
        print("Jarak Bagian Belakang Mobil Kurang Dari 2m")
        print("\n<===     Solusi    ===>")
        print("Tambah Kecepatan!!!")

    #Mengatur Sistem jika semua Bagian dalam jarak aman
    else:
        print("Mobil Dalam Kondisi Aman")
        koneksi.close()


if __name__ == '__main__':
    pipaIn, pipaOut = Pipe()
    JarakKanan = Process(target=kanan,args=(pipaIn,))
    JarakKiri = Process(target=kiri,args=(pipaIn,))
    JarakDepan = Process(target=depan,args=(pipaIn,))
    JarakBelakang = Process(target=belakang,args=(pipaIn,))
    SensorSistem = Process(target=MainControl,args=(pipaOut))

    JarakKanan.start()
    JarakKiri.start()
    JarakDepan.start()
    JarakBelakang.start()
    SensorSistem.start()

    JarakKanan.join()
    JarakKiri.join()
    JarakDepan.join()
    JarakBelakang.join()
    SensorSistem.join()
