# 2419 Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums):
        positiveIndex = 0
        negativeIndex = 1
        res = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[positiveIndex] = nums[i]
                positiveIndex +=2
            else:
                res[negativeIndex] = nums[i]
                negativeIndex+=2
        return res