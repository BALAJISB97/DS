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