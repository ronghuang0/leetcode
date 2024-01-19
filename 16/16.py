# 16. 3Sum Closest

# two pointer
# O(n^2) time, O(logn) or O(n) space depending on sort
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if target == s:
                    return s
                if abs(res-target) > abs(s-target):
                    res=s
                if target < s:
                    right-=1
                else:
                    left+=1
        return res

# binary search
import math
class Solution:
    def threeSumClosest(self, nums, target):
        def search(l, r, t):
            while l<r:
                mid = math.ceil((l+r)/2)
                if nums[mid] <= t:
                    l = mid
                else:
                    r = mid-1
            return l+1
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                tar = target-nums[i]-nums[j]
                hi = search(j+1, len(nums)-1, tar)
                lo = hi-1
                if hi<len(nums) and abs(diff) > abs(target - nums[hi]-nums[i]-nums[j]):
                    diff = target - nums[hi]-nums[i]-nums[j]
                if lo>j and abs(diff) > abs(target - nums[lo]-nums[i]-nums[j]):
                    diff = target - nums[lo]-nums[i]-nums[j]
        return  target-diff
                