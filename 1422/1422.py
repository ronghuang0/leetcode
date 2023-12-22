# 1422. Maximum Score After Splitting a String

# one pass
# s = left0 - total1 - left1
class Solution:
    def maxScore(self, s: str) -> int:
        ones=0
        zeros=0
        diff=-1
        for i in range(len(s)-1):
            if s[i]=='1':
                ones+=1
            else:
                zeros+=1
            diff=max(diff, zeros-ones)
        if s[-1]=='1':
            ones+=1
        return diff+ones