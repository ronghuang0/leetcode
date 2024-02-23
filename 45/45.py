#45. Jump Game II

# time: O(n) space: O(1)
class Solution:
    def jump(self, nums):
        n = len(nums)
        count = 0
        currentEnd = 0
        nextEnd = 0
        for i in range(n-1):
            nextEnd = max(nextEnd, i+nums[i])
            if i == currentEnd:
                currentEnd = nextEnd
                count+=1
        return count
