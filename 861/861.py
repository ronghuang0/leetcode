# 861. Score After Flipping Matrix

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=m*pow(2,n-1)
        for j in range(1, n):
            ones=0
            for i in range(m):
                if grid[i][j]==grid[i][0]:
                    ones+=1
            res+=max(ones, m-ones)*pow(2,n-1-j)
        return res