# 1074. Number of Submatrices That Sum to Target

# time: O(m^2*n^2)
# space: O(m*n)
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top = mat[i-1][j] if i-1>=0 else 0
                left = mat[i][j-1] if j-1>=0 else 0
                diag = mat[i-1][j-1] if min(i-1,j-1)>=0 else 0
                mat[i][j] = matrix[i][j]+ top + left - diag
        res = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        top = mat[r1-1][c2] if r1-1>=0 else 0
                        left = mat[r2][c1-1] if c1-1>=0 else 0
                        diag = mat[r1-1][c1-1] if min(r1-1,c1-1)>=0 else 0
                        total = mat[r2][c2] - top - left + diag
                        if total == target:
                            res+=1
        return res

# prefix sum
# time: O(m^2*n)
# space: O(m*n)
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top = mat[i-1][j] if i-1>=0 else 0
                left = mat[i][j-1] if j-1>=0 else 0
                diag = mat[i-1][j-1] if min(i-1,j-1)>=0 else 0
                mat[i][j] = matrix[i][j]+ top + left - diag
        res = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                h = defaultdict(int)
                h[0] = 1
                for c in range(n):
                    top = mat[r1-1][c] if r1-1>=0 else 0
                    sum = mat[r2][c]-top
                    if sum-target in h:
                        res+=h[sum-target]
                    h[sum]+=1
        return res