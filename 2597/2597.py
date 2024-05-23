# 2597. The Number of Beautiful Subsets

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        m=defaultdict(int)
        res=0
        def dfs(index):
            if index==len(nums):
                return
            for i in range(index, len(nums)):
                target1=nums[i]+k
                target2=nums[i]-k
                if m[target1] ==0 and m[target2]==0:
                    nonlocal res
                    res+=1
                    m[nums[i]]+=1
                    dfs(i+1)
                    m[nums[i]]-=1
        dfs(0)
        return res
