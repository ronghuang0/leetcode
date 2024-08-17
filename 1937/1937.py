# 1937. Maximum Number of Points with Cost

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m=len(points)
        n=len(points[0])
        left=[0]*n
        right=[0]*n
        res=[points[0][i] for i in range(n)]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    left[j]=res[j]
                else:
                    left[j]=max(left[j-1]-1, res[j])
            for j in range(n-1, -1, -1):
                if j==n-1:
                    right[j]=res[j]
                else:
                    right[j]=max(right[j+1]-1, res[j])
            for j in range(n):
                res[j]=max(left[j], right[j])+points[i][j]
        return max(res)
