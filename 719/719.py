# 719. Find K-th Smallest Pair Distance

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # if there are X smaller or == and X>k, then we know the answer
        # is False 
        # so we look for last one that is True numSmaller <=k
        nums.sort()
        def numSmallerEqual(x):
            l=0
            res=0
            for i in range(1, len(nums)):
                while (nums[i]-nums[l])>x:
                    l+=1
                res+=i-l
            return res
        
        l=0
        r=nums[len(nums)-1]-nums[0]
        while l<r:
            mid=(l+r)//2            
            if numSmallerEqual(mid)>=k:
                r=mid
            else:
                l=mid+1
        return l
