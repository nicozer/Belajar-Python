print ("\n\nINGWE IANNICO")
print ("1461600214")

def ganjil():
  print ("\nIni Adalah Hasil Bilangan Ganjil")
  for ganjil in range(10):
    if(ganjil % 2 == 1):
      print (ganjil)

def genap():
  print ("\nIni Adalah Hasil Bilangan Genap")
  for genap in range(50,60,1):
    if(genap % 2 == 0):
      print (genap)

def acak():
  print ("\nIni adalah Hasil Bilangan Acak")
  import random
  for i in range(5):
    print (random.randrange(100, 500))

ganjil()
genap ()
acak()