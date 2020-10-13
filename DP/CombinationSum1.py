class Solution:
    def combinationSum(self, c, target):
        dp=[[] for _ in range(target+1)]
        for i in c:
            for x in range(1,target+1):
                if i > x: continue
                elif i==x: dp[x].append([i])
                else:
                    for lists in dp[x-i]:
                        dp[x].append(lists+[i])
        return dp[target]
s=Solution()        
print(s.combinationSum([2,3,6,7],7))