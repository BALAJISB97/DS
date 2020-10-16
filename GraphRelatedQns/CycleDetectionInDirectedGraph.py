class Solution:
    def canFinish(self, nums, pre):
        self.adj=[[] for _ in range(nums)]
        for i in pre:
            a,b=i
            self.adj[a].append(b)
        self.visited=[0]*nums
        #print(self.adj)
        for i in range(nums):
            if self.visited[i]==0 and not (self.dfs(i)):
                return False
        return True
    def dfs(self,i):
        if self.visited[i]==1:
            return False
        self.visited[i]=1
        for nbr in self.adj[i]:
            if not self.dfs(nbr):return False
        self.visited[i]=2
        return True
        
s=Solution()
print(s.canFinish(2,[[0,1]]))