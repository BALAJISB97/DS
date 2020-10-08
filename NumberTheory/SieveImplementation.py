from math import sqrt
import time
def PrimeNumbers(r):
    s=time.time()
    dp=[1]*r
    primes=[]
    dp[0]=dp[1]=0
    dp[2]=1
    for i in range(2,int((sqrt(r))+1)):
        if dp[i]:
            for j in range(i*i,r,i):
                dp[j]=0
    for i in range(2,r):
        if dp[i]:
            primes.append(i)
            print(i,end=" ")
    e=time.time()
    print("\n Total Time taken :",e-s)
    return primes

#PrimeNumbers(34)
def ReturnKthPrimeNumber(k):
    v=PrimeNumbers(k*k)
    print(v)
    return v[k-1]

print(ReturnKthPrimeNumber(111))
