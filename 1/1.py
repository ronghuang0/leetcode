# 1. Two Sum

# 2 pass
# O(n) space and time
class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            map[nums[i]]=i
        for i in range(len(nums)):
            t = target-nums[i]
            if t in map and map[t] != i:
                return [i, map[t]]
        

# 1 pass
class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            t = target-nums[i]
            if t in map:
                return [i, map[t]]
            map[nums[i]]=i