#array=[2,5,3,4] ts=12
#output the subset 5,3,4
def IsSubsetAvailable(arr,s):
    arr.insert(0,0)
    n=len(arr)
    #Let's initialize the linear space dp:
    dp=[0]*(s+1)
    dp[0]=1
    for i in range(1,n):
        for j in range(s,1,-1):
            if arr[i] > j:
                break
            elif arr[i]<=j:
                print(arr[i],j,j-arr[i])
                need=j-arr[i]
            
                if dp[need]:
                    if not dp[j]:
                        dp[j]=arr[i]
    print(dp)
    if dp[s]:
        ans=[]
        i=s
        while(i>0):
            ans.append(dp[i])
            i=i-dp[i]
    print(ans)
            
IsSubsetAvailable([2,3,6,7],7)