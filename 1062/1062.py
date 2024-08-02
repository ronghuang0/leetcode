# 1062. Longest Repeating Substring

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        def hasSub(size):
            visited=set()
            for i in range(0, n-size+1):
                curr = s[i:i+size]
                if curr in visited:
                    return True
                visited.add(curr)
            return False
        l=0
        r=n-1
        while l<r:
            m=(l+r+1)//2
            if hasSub(m):
                l=m
            else:
                r=m-1
        return l