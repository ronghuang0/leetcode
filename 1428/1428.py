# 1428. Leftmost Column with at Least a One

# move left and down
# O(n+m)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        row, col = binaryMatrix.dimensions()
        r = 0
        c = col-1
        while c >= 0 and r<row:
            while  c>=0 and binaryMatrix.get(r, c) == 1:
                c-=1
            r+=1
        if c == col-1:
            return -1
        return c+1
    
# binary search
# O(nlog(m))
class Solution:
    def search(self, binaryMatrix, row, col):
        l = 0
        r = col
        while l<r:
            mid = (l+r)//2
            if binaryMatrix.get(row, mid) == 1:
                r = mid
            else:
                l = mid+1
        return l
    def leftMostColumnWithOne(self, binaryMatrix):
        row, col = binaryMatrix.dimensions()
        ans = float('inf')
        for r in range(row):
            c = self.search(binaryMatrix, r, col)
            if c < col:
                ans = min(ans, c)
        return -1 if ans == float('inf') else ans