class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        #Initialize graph
        m=[[-1]*n for _ in range(n)]
        rv=[]
        for items in edges:
            m[items[0]][items[1]]=1
        for c in range(n):
            rnode=True
            for r in range(n):
                if m[r][c]!=1:
                    continue
                else:
                    rnode=False
                    break
            if rnode:
                rv.append(c)
        return rv
        #Matrix Approach takes > 7500 ms
#List approach takes 130 ms
#Approach is to find the vertices with zero indegress. In other terms, the node 
#that we won't be able to visit from other nodes.
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
       
        
        d, ans = {}, []
        for x,y in edges:
            d[y]=True
        
        for x in range(n):
            if x not in d:
                ans.append(x)
        return ans
		