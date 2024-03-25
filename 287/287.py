# 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 3 4 2 2
        # count (1,2,3,4) 1,3,4,5
        l=1
        r=len(nums)-1
        while l<r:
            count=0
            mid=(l+r)//2
            for n in nums:
                if n<=mid:
                    count+=1
            if count>mid:
                r=mid
            else:
                l=mid+1
        return l

class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare