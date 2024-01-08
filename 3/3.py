# 3. Longest Substring Without Repeating Characters

# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        map = {}
        ans = 0
        left = 0
        for i in range(len(s)):
            while s[i] in map:
                del map[s[left]]
                left+=1
            map[s[i]]=i
            ans = max(ans, i-left+1)
        return ans
    
# no need to delete map
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        ans = 0
        left = 0
        for i, char in enumerate(s):
            if char in map and left<=map[char]:
                left=map[char]+1
            map[char]=i
            ans = max(ans, i-left+1)
        return ans