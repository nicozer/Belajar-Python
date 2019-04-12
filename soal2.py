import random
import multiprocessing
import time

def ganjil():
	x=[1,2,3,4,5,6,7,8,9,10]
	for a in x:
		print ('Data List---',a)
		time.sleep(random.randrange(1,2))
		print ('Data List Kuadrat---',a**2)
		time.sleep(random.randrange(1,2))
		
		
if __name__ == '__main__':
	worker1 = multiprocessing.Process(target=ganjil)
	worker1.start()
	worker1.join()
	