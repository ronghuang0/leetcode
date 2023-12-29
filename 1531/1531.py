# 1531. String Compression II

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dfs(i, prev, count, k):
            if k<0:
                return float('inf')
            if i==len(s):
                return 0
            if prev == s[i]:
                l = 1 if count in [1, 9, 99] else 0
                return l+dfs(i+1, prev, count+1, k)
            else:
                keep = 1+dfs(i+1, s[i], 1, k)
                remove = dfs(i+1, prev, count, k-1)
                return min(keep, remove)
        return dfs(0, '', 0, k)