# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(curr, index):
            if index==len(nums):
                res.append(curr)
                return
            res.append(curr)
            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(curr.copy(),i+1)
                curr.pop()
        dfs([], 0)
        return res
