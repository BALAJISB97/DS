'''
Leetcode 168
Time Complexity : O(1) and space complexity O(n) for recurise calls
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
'''
class Solution:
    def rer(self,n,s):
        #print('Called Value :',n,s)
        if (n > 26) and ((n//26)<= 26):
            if n%26==0:
                s=s+chr(((n//26)-1)+64)
                s=s+'Z'
                return s
                
            else:
                s=s+chr((n//26)+64)
                s=s+chr((n%26)+64)
                return s
        elif n//26 > 26:
            if n%26==0:
                s=self.rer((n//26)-1,s)
            else:
                s=self.rer(n//26,s)
            if (n%26)!=0:
                s=s+chr((n%26)+64)
            else:
                s=s+'Z'
            return s
        else:
            return s+chr(n+64)
            
            
    def convertToTitle(self, n: int) -> str:
        if n < 0:
            return 
        s=""
        s=self.rer(n,s)
        return s
s=Solution()
print(s.convertToTitle(1300001))