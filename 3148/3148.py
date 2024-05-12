# 3148. Maximum Difference Score in a Grid

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        biggest=[[0]*n for _ in range(m)]
        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                if i+1<=m-1:
                    biggest[i][j] = max(grid[i+1][j], biggest[i+1][j])
                if j+1<=n-1:
                    biggest[i][j]=max(biggest[i][j],grid[i][j+1],biggest[i][j+1])
        res=float('-inf')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1,-1):
                if i==m-1 and j==n-1:
                    continue
                res=max(res, biggest[i][j]-grid[i][j])
        return res