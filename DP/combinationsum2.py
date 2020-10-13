class Solution:
    def combinationSum2(self, candidates, target):
        self.c=sorted(candidates)
        self.t=target
        self.res=[]
        self.backtrack([],self.t,0)
        return self.res
    
    def backtrack(self,path,target,ind):
        if target==0:
            if path not in self.res:
                self.res.append(path)
            return
        if target < 0:
            return 
        
        for i in range(ind,len(self.c)):
            self.backtrack(path+[self.c[i]],target-self.c[i],i+1)

s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''