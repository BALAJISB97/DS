
class Solution:
    def findJudge(self, N,trust):
        
        #MAtrix to represent the connections 
        M=[[-1] * N for _ in range(N)]
        
        #Initialize the connection
        for items in trust:
            M[items[0]-1][items[1]-1]=1
      
        #Find out the Judge by selecting row with -1
        for i in range(N):
            
            Judge=True
            
            for j in  range(N):
                if M[i][j]==-1:
                    continue
                else:
                    Judge=False 
                    break
            
            if Judge:
                Jans=i+1
                Jv=i
                break
        
        if not Judge:
            return -1
        else:
            #check if everyone trusts the judge using trust flag
            for row in range(N):
                t=True
                if row==Jv:
                    continue
                elif M[row][Jv]==1:
                    continue
                else:
                    return -1
            if t:
                return Jans
                
s=Solution()
print(s.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

 

Constraints:

    1 <= N <= 1000
    0 <= trust.length <= 10^4
    trust[i].length == 2
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N
'''