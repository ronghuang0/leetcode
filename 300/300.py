# 300. Longest Increasing Subsequence

# append -10^4 to the end of nums and use it as a prev
class Solution:
    def lengthOfLIS(self, nums):
        prev = [0]*(len(nums)+1)
        nums.append(-10**4-1)
        for i in range(len(nums)-1, -1, -1):
            curr = [0]*(len(nums)+1)
            for j in range(len(nums)):
                keep = 0
                if nums[i] > nums[j]:
                    keep = 1+prev[i]
                skip = prev[j]
                curr[j] = max(keep, skip)
            prev=curr
        return max(prev)
    

# the last element in every row stores the result when the prev is -inf
class Solution:
    def lengthOfLIS(self, nums) -> int:
        prev = [0]*(len(nums)+1)
        for i in range(len(nums)-1, -1, -1):
            curr = [0]*(len(nums)+1)
            for j in range(i):
                keep = 0
                if nums[i] > nums[j]:
                    keep = 1+prev[i]
                skip = prev[j]
                curr[j] = max(keep, skip)
            curr[len(nums)] = max(1+prev[i], prev[len(nums)])
            prev=curr
        return max(prev)

# 1d dfs - each call represents longest sub from that point that includes index
class Solution:
    def lengthOfLIS(self, nums):
        dp=[None]*len(nums)
        def dfs(index):
            if index == len(nums):
                return 0
            if dp[index]:
                return dp[index]
            m=1
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index]:
                    m = max(m, 1+dfs(i))
            dp[index] = m
            return m
        ans = 0
        for j in range(len(nums)):
            ans=max(ans, dfs(j))
        return ans
    
# patience sort
class Solution:
    def search(self, arr, target):
        left=0
        right=len(arr)-1
        while left<right:
            mid = (left+right)//2
            if arr[mid] < target:
                left = mid+1
            else:
                right = mid
        return left
    def lengthOfLIS(self, nums):
        l = []
        for n in nums:
            if not l or n>l[-1]:
                l.append(n)
            else:
                i = self.search(l, n)
                l[i] = n
        return len(l)