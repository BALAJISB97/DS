class Solution:
    def uniquePaths(self,m,n):
        dp=[[1]*n for _ in range(m)]
        print(dp)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if i==0:
                    print('values',dp[i][j+1],'down=',dp[i+1][j])
                ans=dp[i][j+1]+dp[i+1][j]
                print(i,j,ans)
                dp[i][j]=ans
        print(dp)
        
        return dp[0][0]
s=Solution()
print(s.uniquePaths(10,10))