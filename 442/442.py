# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i, val in enumerate(nums):
            nums[abs(val)-1] *=-1
        res=[]
        for n in nums:
            if nums[abs(n)-1] >0:
                res.append(abs(n))
                nums[abs(n)-1]*=-1
        return res