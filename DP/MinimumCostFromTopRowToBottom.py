"""
5 1 2 6 Starting from any cell in this row, find out minimum val/cost to reach any cell in the last row.
9 9 7 5
3 1 4 8
you can right or down,downleft downright.
"""
def MinimumCost(arr):
    r=len(arr)
    c=len(arr[0])
    dp=[[0]*(c) for _ in range(r-1)]
    a=[]
    for i in range(c):
        a.append(arr[r-1][i])
    dp.append(a)
    print(dp)
    #Lets initialize dp
    for i in range(r-2,-1,-1):
        
        for j in range(c-1,-1,-1):
            #down always exists as we are starting from the last before row to the first row.
            mi=float('inf')
            d=dp[i+1][j]
            mi=min(d,mi)
            #down right
            if i+1 <r and j+1 <c:
                dr=dp[i+1][j+1]
                mi=min(dr,mi)
               

            #down left:
            if i+1<r and j-1 >=0:
                dl=dp[i+1][j-1]
                mi=min(dl,mi)
                
            #right
            if j+1 <c:
                r=dp[i][j+1]
                mi=min(r,mi)
            dp[i][j]=mi+arr[i][j]
    print(dp)
            
MinimumCost([[5,1,2,6],[9,9,7,5],[3,1,4,8]])
