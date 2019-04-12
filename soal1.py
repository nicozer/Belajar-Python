import random
import multiprocessing
import time

def genap():
	for a in range(11,20):
		if a % 2 == 0: print ('Genap---',a)
		time.sleep(random.randrange(1,3))		

def genaplagi():
	for a in range(1,11):
		if a % 2 == 0: print ('GenapLagi---',a)
		time.sleep(random.randrange(1,3))

def ganjil():
	for a in range(50,60):
		if a % 1 == 0: print ('Ganjil---',a)
		time.sleep(random.randrange(1,3))
		
def acak():
	
	for a in range(0,5): print ('Acak---',time.sleep(random.randrange(1,3)),random.randrange(100,200))
	
		
if __name__ == '__main__':
	worker1 = multiprocessing.Process(target=genap)
	worker2 = multiprocessing.Process(target=genaplagi)
	worker3 = multiprocessing.Process(target=ganjil)
	worker4 = multiprocessing.Process(target=acak)	
	worker1.start()
	worker2.start()
	worker3.start()
	worker4.start()
	worker1.join()
	worker2.join()
	worker3.join()
	worker4.join()