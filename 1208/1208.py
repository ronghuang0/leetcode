# 1208. Get Equal Substring Within Budget

# sliding window

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        currCost=0
        maxLength=0
        l=0
        for r in range(n):
            currCost+=abs(ord(s[r])-ord(t[r]))
            if currCost>maxCost:
                currCost-=abs(ord(s[l])-ord(t[l]))
                l+=1
        return r-l+1


# prefix sum + binary search
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        prefix=[]
        sum=0
        for i in range(n):
            sum+=abs(ord(s[i])-ord(t[i]))
            prefix.append(sum)
        res=0
        l=0
        for i in range(n):
            if prefix[i]<=maxCost:
                res=max(res, i+1)
                continue
            r=i
            while l<r:
                mid=(l+r)//2
                if (prefix[i]-prefix[mid])<=maxCost:
                    r=mid
                else:
                    l=mid+1
            res=max(res, i-l)
        return res