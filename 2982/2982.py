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

# for every letter we keep track of the frequencies the lengths for a unique substring
# ex - at index 3 if the value is 3 - that means there were 3 separate substrings that had 
# length of 3 or more. From this we can iterate backwards to get number of substrings for 
# each length. 

class Solution:
    def maximumLength(self, s: str) -> int:
        freqs = [[0]*(len(s)+1) for _ in range(26)]
        streak = 1
        prev = ''
        for char in s:
            if prev == char:
                streak+=1
            else:
                streak=1
            freqs[ord(char)-ord('a')][streak]+=1
            prev = char
        ans = -1
        for f in freqs:
            sum=0
            for length in range(len(f)-1, 0, -1):
                sum+=f[length]
                if sum >= 3:
                    ans = max(ans, length)
                    break
        return ans

# binary search the answer
# for every search we keep track for each letter the number of substrings greater than length

class Solution:
    def maximumLength(self, s: str) -> int:
        def isValid(length):
            arr = [0]*26
            streak = 1
            prev = ''
            for char in s:
                if prev == char:
                    streak+=1
                else:
                    streak=1
                if streak>=length:
                    arr[ord(char)-ord('a')]+=1
                    if arr[ord(char)-ord('a')] == 3:
                        return True
                prev=char
            return False
        l=0
        r=len(s)
        while l<r:
            mid = (l+r+1)//2
            if isValid(mid):
                l=mid
            else:
                r=mid-1
        if l==0:
            return -1
        return l
    
# separate into streak lenghts
# based on the lengths of the 3 top streaks we can calculate the ans

from itertools import groupby
from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        lookup = defaultdict(list)

        for v,g in groupby(s):
            lookup[v].append(len(list(g)))
        ans = -1
        for k, c in lookup.items():
            c.sort(reverse=True)
            if len(c)>=3:
                ans=max(ans, c[2])
            if len(c)>=2:
                if c[0]==c[1]:
                    ans = max(ans, c[0]-1)
                else:
                    ans = max(ans, c[1])
            if len(c)>=1:
                ans = max(ans, c[0]-2)
        if ans <= 0:
            return -1
        return ans