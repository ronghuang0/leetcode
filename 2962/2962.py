# 2962. Count Subarrays Where Max Element Appears at Least K Times

from bisect import bisect

# sliding window
# adding all substrings where left is start of substring
class Solution:
    def countSubarrays(self, nums, k):
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
    def countSubarrays(self, nums, k):
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
    
# prefix sum + binary search
# for each element use bs to look for the first index where the subarray is no longer valid

class Solution:
    def countSubarrays(self, nums, k):
        m = max(nums)
        prefix = []
        c = 0
        for n in nums:
            if n==m:
                c+=1
            prefix.append(c) 
        ans = 0
        for i in range(len(nums)):
            if prefix[i]>=k:
                j = bisect.bisect_left(prefix, prefix[i]-k+1)
                ans+=j+1
        return ans
                