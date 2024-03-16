# 525. Contiguous Array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map={}
        map[0]=-1
        sum=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                sum+=1
            else:
                sum-=1
            if sum in map:
                res=max(res,i-map[sum])
            else:
                map[sum]=i
        return res