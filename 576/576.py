# 576. Out of Boundary Paths

# recursion + memo
# O(m*n*k) space and time
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def inBounds(row, col):
            return 0<=row<m and 0<=col<n
        mod = 10**9+7
        dp = [[[None for _ in range(n)] for _ in range(m+1)] for _ in range(maxMove+1)]
        def dfs(movesLeft, row, col):
            if dp[movesLeft][row][col] is not None:
                return dp[movesLeft][row][col]
            if movesLeft == 0:
                return 0
            res = 0
            neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for nr, nc in neighbors:
                if inBounds(nr, nc):
                    res= (res+dfs(movesLeft-1, nr, nc))%mod
                else:
                    res+=1
            dp[movesLeft][row][col] = res
            return res
        return dfs(maxMove, startRow, startColumn)

# tabulation
# time: O(m*n*k)
# space: O(m*n)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def inBounds(row, col):
            return 0<=row<m and 0<=col<n
        mod = 10**9+7
        prev = [[0]*(n+1) for _ in range(m+1)]
        for k in range(maxMove-1, -1, -1):
            curr = [[0]*(n+1) for _ in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    res = 0
                    neighbors = [(i+1, j), (i-1,j), (i,j+1), (i, j-1)]
                    for nr, nc in neighbors:
                        if inBounds(nr, nc):
                            res = (res+prev[nr][nc])%mod
                        else:
                            res+=1
                    curr[i][j] = res
            prev = curr
        return prev[startRow][startColumn]
    
# bfs with count
# O(m*n) space and time
from collections import defaultdict
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        def isIn(row, col):
            return 0<=row<m and 0<=col<n
        q = defaultdict(int)
        q[(startRow, startColumn)] = 1
        moves = 0
        res = 0
        while moves<maxMove:
            next = defaultdict(int)
            for row, col in q:
                neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                for nr, nc in neighbors:
                    if isIn(nr, nc):
                        next[(nr,nc)]+=q[(row,col)]
                    else:
                        res= (res+q[(row,col)]) % mod
            moves+=1
            q = next
        return res
