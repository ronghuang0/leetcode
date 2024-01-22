# 645. Set Mismatch

# Use - to indicate seen or not
# O(n) time, O(1) space
class Solution:
    def findErrorNums(self, nums):
        zero = None
        two = None
        for n in nums:
            n=abs(n)
            if nums[n-1] < 0:
                two = n-1
            nums[n-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0 and i != two:
                zero = i
        return [two+1, zero+1]
    

# equation 1: sum of nums equation 2: sum of squares
# O(n) time, O(1) space
class Solution:
    def findErrorNums(self, nums):
        o = (1+len(nums))*len(nums)/2
        n = sum(nums)
        x = o-n
        y = 0
        for i in range(1, len(nums)+1):
            y+= i**2 - nums[i-1]**2
        d = (y-x**2)/(2*x)
        m = x+d
        return [int(d),int(m)]

        