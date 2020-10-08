def Binary(base,power):
    res=1
    while(power):
        if power%2:
            power-=1
            res=res*base
        else:
            base=base*base
            power/=2
    return res



print(Binary(2.1000,3))