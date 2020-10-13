class Solution:
    def combinationSum(self, candidates, target):
        self.c=candidates
        self.res=[]
        self.t=target
        self.backtrack([],self.t,0)
        return self.res
        
    def backtrack(self,path,target,ind):
        if target==0:
            self.res.append(path)
            return 
        if target < 0:
            return
        for x in range(ind,len(self.c)):
            self.backtrack(path+[self.c[x]],target-self.c[x],x)
s=Solution()
print(s.combinationSum([2,3,7,6],7))
        
