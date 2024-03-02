# 3043. Find the Length of the Longet Common Prefix

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = {}
        for n in arr1:
            for i in range(len(str(n))):
                prefixes[str(n)[:i+1]]=True
        res = 0
        for n in arr2:
            for i in range(len(str(n))):
                p = str(n)[:i+1]
                if p in prefixes:
                    res = max(res, len(p))
        return res