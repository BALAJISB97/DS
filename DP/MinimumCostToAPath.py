
def MinimumCost(arr):
    """
    Func gives you the minimum cost to reach 1,1 or origin to the end point N,M

    """
    r=len(arr)
    c=len(arr[0])

    dp=[[float('inf')]*(c+1) for _ in range(r+1)]
    #Let's initialize the dp array!
    dp[r-1][c]=0
    dp[r][c-1]=0
    #Let's traverse and find the minimum sum
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            #make a choice down or right:
            val=min(dp[i+1][j],dp[i][j+1])
            print(val)
            dp[i][j]=val+arr[i][j]
    print(dp)
    return dp[0][0]

print(MinimumCost([[5,1,2,6],[9,9,7,5],[3,1,4,8]]))
help(MinimumCost)