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
'''
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

 

Constraints:

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.


'''

