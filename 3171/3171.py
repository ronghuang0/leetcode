# 3171. Find Subarray With Bitwise AND Closest to K

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        curr=[0]*30
        def value(arr, size):
            res=0
            for i in range(30):
                if arr[i]==size:
                    res+=2**(29-i)
            return res
        l=0      
        ans=float('inf')
        for r in range(len(nums)):
            num = bin(nums[r])[2:].zfill(30)
            
            for i in range(len(num)):
                if num[i]=='1':
                    curr[i]+=1
            ans=min(ans, abs(k-value(curr,r-l+1)))
            while l<r and value(curr, r-l+1) < k:
                num = bin(nums[l])[2:].zfill(30)
                l+=1
                for i in range(len(num)):
                    if num[i]=='1':
                        curr[i]-=1
                ans=min(ans, abs(k-value(curr,r-l+1)))
        return ans