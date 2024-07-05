# 918. Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # prefix - starting at 0
        # suffix - starting at end
        n=len(nums)
        # biggest suffix at that index
        maxRight=[None]*n
        maxRight[n-1]=nums[n-1]
        total=nums[n-1]
        for i in range(n-2,-1,-1):
            total+=nums[i]
            maxRight[i]=max(total, maxRight[i+1])
        specialSum=float('-inf')
        curr=0
        for i in range(n-1):
            curr+=nums[i]
            specialSum=max(specialSum, curr+maxRight[i+1])
        
        biggest=float('-inf')
        total=0
        for num in nums:
            total+=num
            biggest=max(biggest, total)
            if total<0:
                total=0
        return max(biggest, specialSum)