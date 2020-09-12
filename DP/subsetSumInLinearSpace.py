#Approach Three, reducing the space complexity to linear space
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
                print(need)
                if dp[need]:
                    if j==11:
                        print('#------------------------#\n,value=',arr[i],i,j)
                    dp[j]=1
    print(dp)

    print(dp)
IsSubsetAvailable([2,5,3,4],12)