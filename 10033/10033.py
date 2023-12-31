# Weekly Contest 378 q3
# 10033. Find Longest Special Substring That Occurs Thrice II

class Solution:
    def maximumLength(self, s: str) -> int:
        streak = 1
        map = defaultdict(int)
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                for j in range(0, streak):
                    sp = s[i-1]+str(j+1)
                    map[sp] += streak-j
                streak = 1
            else:
                streak += 1
        for j in range(0, streak):
            sp = s[-1]+str(j+1)
            map[sp] += streak-j
        ans = -1
        for key, value in map.items():
            if value >= 3:
                ans = max(int(ans), int(key[1:]))
        return ans