# 2962. Count Subarrays Where Max Element Appears at Least K Times

# sliding window
# adding all substrings where left is start of substring
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l=0
        ans=0
        count=0
        for i in range(len(nums)):
            if nums[i] == m:
                count+=1
            while count==k:
                ans+=len(nums)-i
                if nums[l] == m:
                    count-=1
                l+=1
            
        return ans
    
# sliding window
# adding all substring where right is end of substring
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l=0
        ans=0
        count=0
        for i in range(len(nums)):
            if nums[i] == m:
                count+=1
            while count==k:
                if nums[l] == m:
                    count-=1
                l+=1
            ans+=l
        return ans
                