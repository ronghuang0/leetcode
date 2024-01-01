# Weekly Contest 378 q3
# 2982. Find Longest Special Substring That Occurs Thrice II

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

# for each letter we only need to keep track of 3 longest substrings
# for s[i] we treat it as the streak ending on s[i] and if the streak
# is longer than the min streak we replace it
# once a streak reaches 3rd largest - that means it is present in the
# string 3 times
class Solution:
    def maximumLength(self, s: str) -> int:
        freqs = [[-1,-1,-1] for _ in range(26)]
        streak = 0
        prev = ''
        for char in s:
            if char == prev:
                streak+=1
            else:
                streak=1
            curr = ord(char)-ord('a')
            m = min(freqs[curr])
            i = freqs[curr].index(m)
            if streak > m:
                freqs[curr][i] = streak
            prev = char
        ans = -1
        for f in freqs:
            ans = max(ans, min(f))
        return ans