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
'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5

"""
