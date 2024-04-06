# 1249. Minimum Remove to Make Valid Parenthesis

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count=0
        stack=[]
        for v in s:
            if v==')' and count==0:
                continue
            if v=='(':
                count+=1
            if v==')':
                count-=1
            stack.append(v)
        count=0
        res=''
        for v in reversed(stack):
            if v=='(' and count==0:
                continue
            if v=='(':
                count-=1
            if v==')':
                count+=1
            res= v+res
        return res
                    
                    

                
                
                