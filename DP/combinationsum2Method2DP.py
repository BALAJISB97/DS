class Solution:
    def combinationSum2(self, candidates, target):
        self.c=sorted(candidates)
        self.t=target
        self.res=[]
        dp=[[] for _ in range(target+1)]
        for val in self.c:
            for x in range(target,0,-1):
                if val == x:
                    if [val] not in dp[x]:
                        dp[x].append([val])
                elif val > x:
                    break
                else:
                    for lists in dp[x-val]:
                        if lists+[val] not in dp[x]:
                            dp[x].append(lists+[val])
            #print(val, dp)
        return dp[target]
s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))