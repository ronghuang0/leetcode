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

# xor original and new results in the xor of missing and duplicate
# we can choose any 1 bit out of the resulting xor
# divide into two groups - 1 at that bit and 0 at that bit
# in each group the xor of all the numbers leaves an answer
# this is because we know our two numbers will have difference in that bit and be in separate groups and
# every number will be in the same set as it's clone - so in each set our numbers are the only unique ones
# O(n) time, O(1) space
class Solution:
    def findErrorNums(self, nums):
        xor = 0
        for i, num in enumerate(nums):
            xor ^= (i+1)^num
        bit = xor & ~(xor-1)
        zero, one = 0, 0
        for num in nums:
            if (num & bit) != 0:
                one^=num
            else:
                zero^=num
        for i in range(1, len(nums)+1):
            if (i & bit) != 0:
                one^=i
            else:
                zero^=i
        for num in nums:
            if zero == num:
                return [zero, one]
        return [one, zero]

        