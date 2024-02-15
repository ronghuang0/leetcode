# 2971. Find Polygon With the largest Perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        total = [0]*n
        total[0] = nums[0]
        for i in range(1,n):
            total[i] = total[i-1]+nums[i]
        res = -1
        for i in range(2, n):
            if total[i-1]>nums[i]:
                res = max(res, total[i])
        return res