# 1289. Minium Path Falling Sum II

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min=float('inf')
        secondMin=float('inf')
        minIndex=None
        secondMinIndex=None
        for c in range(n):
            if grid[0][c]<=min:
                secondMin=min
                secondMinIndex=minIndex
                min=grid[0][c]
                minIndex=c
            elif grid[0][c]<=secondMin:
                secondMin=grid[0][c]
                secondMinIndex=minIndex
        
        for r in range(1,n):
            nextMin=float('inf')
            nextSecondMin=float('inf')
            nextMinIndex=None
            nextSecondMinIndex=None
            for c in range(n):
                if c!=minIndex:
                    if (min+grid[r][c]) <= nextMin:
                        nextSecondMin=nextMin
                        nextSecondMinIndex=nextMinIndex
                        nextMin=min+grid[r][c]
                        nextMinIndex=c
                    elif (min+grid[r][c]<=nextSecondMin):
                        nextSecondMin=min+grid[r][c]
                        nextSecondMinIndex=c
                else:
                    if (secondMin+grid[r][c])<=nextMin:
                        nextSecondMin=nextMin
                        nextSecondMinIndex=nextMinIndex
                        nextMin=secondMin+grid[r][c]
                        nextMinIndex=c
                    elif (secondMin+grid[r][c]<=nextSecondMin):
                        nextSecondMin=secondMin+grid[r][c]
                        nextSecondMinIndex=c
            min=nextMin
            minIndex=nextMinIndex
            secondMin=nextSecondMin
            secondMinIndex=nextSecondMinIndex
           
        return min



      
        