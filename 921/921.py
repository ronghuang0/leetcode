# Minimum Add to Make Parenthesis Valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        res=0
        for char in s:
            if char==')':
                if count>0:
                    count-=1
                else:
                    res+=1
            else:
                count+=1
        return res+count
