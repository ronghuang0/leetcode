# 3148. Maximum Difference Score in a Grid

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=float('-inf')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                greatest=float('-inf')
                if i<m-1:
                    greatest=max(greatest, grid[i+1][j])
                if j<n-1:
                    greatest=max(greatest, grid[i][j+1])
                res=max(res, greatest-grid[i][j])
                grid[i][j]=max(greatest, grid[i][j])
        return res