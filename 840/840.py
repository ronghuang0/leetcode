# 840. Magic Squares in Grid

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])    

        def scanBox(r,c):
            visited=set()
            for i in range(3):
                for j in range(3):
                    if grid[r+i][c+j] in visited or grid[r+i][c+j] > 9 or grid[r+i][c+j]<1:
                        return False
                    visited.add(grid[r+i][c+j])
            diag1=grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]
            diag2=grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]
            if diag1!=diag2:
                return False
            row1=grid[r][c]+grid[r][c+1]+grid[r][c+2]
            row2=grid[r+1][c]+grid[r+1][c+1]+grid[r+1][c+2]
            row3=grid[r+2][c]+grid[r+2][c+1]+grid[r+2][c+2]
            if diag1!=row1 or diag1!=row2 or diag1!=row3:
                return False
            col1=grid[r][c]+grid[r+1][c]+grid[r+2][c]
            col2=grid[r][c+1]+grid[r+1][c+1]+grid[r+2][c+1]
            col3=grid[r][c+2]+grid[r+1][c+2]+grid[r+2][c+2]
            if diag1!=col1 or diag1!=col2 or diag1!=col3:
                return False
            return True
        res=0
        for i in range(m-2):
            for j in range(n-2):
                if scanBox(i,j):
                    res+=1
        return res
        
            
