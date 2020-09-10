import math
def masking(s):
    n=len(s)
    op=[]
    t=1<<n # Same as 2 ^ n 2**n
    for i in range(t):
        a=""
        for j in range(n):
            f=1<<j
            print(j,f,j&f)
            if ((i & f) !=0):
                a=a+s[j]
        op.append(a)
    return op



print(masking('abcd'))
