def matrixprinter(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],' ',end="")
        print()
#TimeComplexity O(2(n*m)) space complexity O(n*m)
def isSubsetSumAvailable(arr,sum):
    n=len(arr)
    m=sum
    arr.insert(0,0)
    print(arr)
    dp=[[0]*(m+1) for _ in range (n+1)]
    #Let's make the some initial assignment to the dp table
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(0,m+1):
            if j < arr[i]:
                dp[i][j]=dp[i-1][j]
            else:
                need=j-arr[i]
                if dp[i-1][j]==1 or dp[i-1][need]==1:
                    dp[i][j]=1
                else:
                    dp[i][j]=0
    matrixprinter(dp)
    return dp[n][m]


    

    
print(isSubsetSumAvailable([2,5,3 ,4],12))