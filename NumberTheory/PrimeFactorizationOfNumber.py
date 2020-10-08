import time
from math import sqrt
def Factors(n):
    s=time.time()
    t=n
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            cnt=0
            while(n%i==0):
                n=n/i
                #print(n)
                cnt+=1
            print(i,"^",cnt, end=" |")
    e=time.time()
    if n > 1:
        print(n,"^",1)
    print("\n Total Time taken :",e-s)
Factors(47)