# 2444. Count Subarrays With Fixed Bounds

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mini=-1
        maxi=-1
        start=0
        res=0
        for i, val in enumerate(nums):
            if val<minK or val>maxK:
                start=i+1
                mini=-1
                maxi=-1
            else:
                if val==minK:
                    mini=i
                if val==maxK:
                    maxi=i
                if mini!=-1 and maxi!=-1:
                    res+=min(maxi,mini)-start+1
        return res