import random
import array as larik

hasil = 0

MyList=[0,0,0,0,0,0,0]
for i in range(0,1000):
    b= random.randrange(6)+1
    #print(b)
    MyList[b]+=1
    #print(b,':',MyList[b]

for i in range(1,7):
    print ('Dadu-',i,':',MyList[i])
    hasil+=MyList[i]

print ("Total: ",hasil)