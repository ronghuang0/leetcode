class Solution:
    # 54. Spiral Matrix
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs=[(0,1), (1,0), (0,-1), (-1,0)]
        dir = 0
        m=len(matrix)
        n=len(matrix[0])
        ans = []
        visited=set()
        r=0
        c=0
        def inBounds(row, col):
            return row<m and col<n and col>=0 and not (row,col) in visited
        count=0
        while count<m*n:
            if inBounds(r, c):
                ans.append(matrix[r][c])
                visited.add((r,c))
                count+=1
            else:
                r-=dirs[dir][0]
                c-=dirs[dir][1]
                dir=(dir+1)%4
            r+=dirs[dir][0]
            c+=dirs[dir][1]
        return ans

