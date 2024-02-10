# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        for gap in range(len(s)):
            for i in range(len(s)-gap):
                j = i+gap
                if s[i] == s[j]:
                    if (i+1) >= (j-1):
                        dp[i][j] = True  
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j]==True:
                        res+=1
        return res