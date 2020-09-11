def MininmumNumberofCoins(denom,sum):
    print(sum)
    if sum==0:
        return 0
    if sum==-1:
        return -1
    c=0
    sorted(denom)
    if sum >=denom[len(denom)-1]:
        v=MininmumNumberofCoins(denom,sum-denom[len(denom)-1])
        c=c+1+v
    elif sum >= denom[1]:
        v=MininmumNumberofCoins(denom,sum-denom[1])
        c=c+1+v
    elif sum >= denom[0]:
        v=MininmumNumberofCoins(denom,sum-denom[0])
        c=c+1+v
    else:
        return -1
    return c
print(MininmumNumberofCoins([1,2,5],18))