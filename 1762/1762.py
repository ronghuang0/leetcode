# 1762. Tuple With Same Product

# O(n^2) space and time
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums):
        map = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res+=8*map[nums[i]*nums[j]]
                map[nums[i]*nums[j]]+=1
        return res