# 76. Minimum Window Substring

#O(n) space and time
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        need = len(c)
        have = 0
        left = 0
        res = [-1,-1]
        length = float('inf')
        for right in range(len(s)):
            if s[right] not in c:
                continue
            c[s[right]]-=1
            if c[s[right]] == 0:
                have+=1
            while need == have:
                if right-left+1 < length:
                    res = [left, right]
                    length = right-left+1
                if s[left] not in c:
                    left+=1
                    continue
                c[s[left]]+=1
                if c[s[left]] == 1:
                    have-=1
                left+=1
        return '' if res[0]==-1 else s[res[0]:res[1]+1] 