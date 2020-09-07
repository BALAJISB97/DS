class Solution:
    def maxLevelSum(self, root):
        q=[]
        temp=root
        q.append(temp)
        q.append('#')
        ms=float("-inf")
        lv=1
        la=0
        ls=0
        while(len(q)!=0):
            
            node=q.pop(0)
            if node=='#' and len(q)==0:
                break
            
            if node=='#' and len(q)!=0:
                if ms < ls:
                    ms=ls
                    la=lv
                ls=0
                lv+=1
                q.append('#')
                continue
            
            if node!='#':
                ls+=node.val
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return la
'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
'''