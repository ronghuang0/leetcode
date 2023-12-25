# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[1]*(len(s)+1)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i]=0
                continue
            if i==len(s)-1:
                dp[i]=1
                continue
            res = dp[i+1]
            if int(s[i]+s[i+1]) <= 26:
                res+=dp[i+2]
            dp[i]=res
        return dp[0]