# Weekly Contest 376 q4
# 2968. Apply Operations to Maximize Frequency

# sliding window
# the cost is the right half minus the left half
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        c=0
        res=0
        for r in range(len(nums)):
            c+=nums[r]-nums[(r+l)//2]
            while c > k:
                c-=nums[(r+l+1)//2]-nums[l]
                l+=1
            res=max(res, r-l+1)
        return res
    
# binary search
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        sums = list(accumulate(nums, initial=0))
        def isPossible(l):
            for i in range(len(nums)-l+1):
                if l%2==0:
                    costLeft=nums[i+l//2-1]*(l//2)-(sums[i+l//2]-sums[i])
                    costRight=(sums[i+l]-sums[i+l//2])-nums[i+l//2-1]*(l//2)
                    if(costLeft+costRight <= k):
                        return True
                else:
                    costLeft = nums[i+l//2]*(l-1)//2-(sums[i+l//2]-sums[i])
                    costRight=(sums[i+l]-sums[i+l//2+1])-nums[i+l//2]*(l-1)//2
                    if(costLeft+costRight <= k):
                        return True
            return False
        left =0
        right = len(nums)
        while(left<right):
            mid = math.ceil((left+right)/2)
            if(isPossible(mid)):
                left=mid
            else:
                right=mid-1
        return left