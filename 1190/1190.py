# 1190. Reverse Substrings Between Each Pair of Parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs=[None]*len(s)
        parenStack=[]
        for i,char in enumerate(s):
            if char=='(':
                parenStack.append(i)
            if char==')':
                last=parenStack.pop()
                pairs[i]=last
                pairs[last]=i
        dir = 1
        index=0
        res=[]
        while index<len(s):
            if s[index]=='(' or s[index]==')':
                dir*=-1
                index=pairs[index]+dir
            else:
                res.append(s[index])
                index+=dir
        return ''.join(res)

