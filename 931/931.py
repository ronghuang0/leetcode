# 931. Minimum Falling Path Sum

# O(n^2) space and time
from functools import cache
class Solution:
    def minFallingPathSum(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        def inBounds(r, c):
            return 0<=r<m and 0<=c<n
        @cache
        def dfs(r, c):
            if r == m-1:
                return matrix[r][c]
            candidates = [(r+1, c-1), (r+1, c), (r+1, c+1)]
            res = float('inf')
            for row, col in candidates:
                if inBounds(row, col):
                    res=min(res, matrix[r][c]+dfs(row, col))
            return res
        ans = float('inf')
        for j in range(n):
            ans = min(ans, dfs(0, j))
        return ans
    
# O(n^2) time, O(n) space
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def inBounds(r, c):
            return 0<=r<m and 0<=c<n
        prev = matrix[-1].copy()
        for i in range(m-2, -1, -1):
            curr = [0]*n
            for j in range(n):
                res = float('inf')
                candidates = [(i+1, j), (i+1, j+1), (i+1, j-1)]
                for row, col in candidates:
                    if inBounds(row, col):
                        res = min(res, prev[col])
                curr[j] = matrix[i][j] + res
            prev = curr
        return min(prev)