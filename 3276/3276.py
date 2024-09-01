# 3276. Select Cells in Grid With Maximum Score

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        for g in grid:
            g.sort(reverse=True)
        # lookup[i][k]
        # row i, score k
        # stores the first val  that is <k
        lookup=[[n]*102 for i in range(m)]
        for k in range(102):
            for i in range(m):
                for j in range(n):
                    if grid[i][j]<k:
                        lookup[i][k]=j
                        break
        # last - last value chosen
        # b - bitmap representation of state
        @cache
        def dfs(last, b):
            res=0
            for i in range(m):
                if (1<<i)&b==0:
                    index=lookup[i][last]
                    if index<n:
                        res=max(dfs(grid[i][index], (1<<i)|b)+grid[i][index], res)
            return res
        return dfs(101, 0)
