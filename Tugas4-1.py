a=10

def kirim():
    b=15
    global c
    c=25
    print("1.Modul kirim nilai : a,b,c : ", a,b,c)

def terima():
    print("2.Modul terima nilai : a,b,c : ", a,b,c)

b = 10

kirim()
terima()

print("3.Diluar modul : nilai a,b,c : ", a, b, c)