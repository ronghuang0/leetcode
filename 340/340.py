# 340. Longest Substring with at Most K Distinct Characters

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        f=defaultdict(int)
        distinct=0
        start=0
        res=0
        for end, val in enumerate(s):
            f[val]+=1
            if f[val]==1:
                distinct+=1
            if distinct>k:
                f[s[start]]-=1
                if f[s[start]]==0:
                    distinct-=1
                start+=1
            res=end-start+1
        return res