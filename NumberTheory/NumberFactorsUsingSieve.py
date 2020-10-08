dp=[-1]*10000
def sieve(n):
    for i in range(2,n+1):
        if dp[i]==-1:
            for j in range(i,n+1,i):
                dp[j]=i
def factors(n):
    sieve(n)
    f=[]
    print(dp)
    while(n>=1):
        f.append(dp[n])
        n=n//dp[n]
    return f
print(factors(786))
        