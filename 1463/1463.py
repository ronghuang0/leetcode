# 1463. Cherry Pickup II
# O(mn^2) space and time
from functools import cache
class Solution:
    def cherryPickup(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def dfs(i,j,k):
            if i == m-1:
                if j == k:
                    return grid[i][j]
                print(i,j,k)
                return grid[i][j]+grid[i][k]
            leftNeighbors = [j-1,j,j+1]
            rightNeighbors = [k-1,k,k+1]
            res = 0
            for x in leftNeighbors:
                for y in rightNeighbors:
                    if x<0 or x>=n or y<0 or y>=n:
                        continue
                    res = max(res, dfs(i+1, x, y))
            res += grid[i][j]
            if j != k:
                res+=grid[i][k]
            return res
        return dfs(0, 0, n-1)