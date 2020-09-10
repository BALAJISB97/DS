def isSubsetSumMatches(arr,targetSum):
    n=len(arr)
    t=1<<n #Total Combinations possible
    for i in range(t):
        s=0
        for j in range(n):
            f=1<<n
            if i&j:
                s+=arr[j]
        
        if s==targetSum:
            return True
    return False
print(isSubsetSumMatches([3,2,0,7,-1],8))
print(isSubsetSumMatches([-1,3,3],4))
print(isSubsetSumMatches([4,5,-1],5))
            

