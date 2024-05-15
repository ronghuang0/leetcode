# 2812. Find the Safest Path in a Grid

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        # find score for each point. Start from thieves and spread
        arr=deque()
        # row, col, safety score
        scores=[[-1]*n for _ in range(n)]
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    arr.append((i,j,0))
                    grid[i][j]=0
        while arr:
            r,c,score=arr.popleft()
            if r<0 or r>=n or c<0 or c>=n:
                continue
            if scores[r][c] != -1:
                continue
            scores[r][c]=score
            for dr,dc in neighbors:
                arr.append((dr+r, dc+c, score+1))
        
        # safety, row, col
        h=[(-scores[0][0], 0,0)]
        res=float('inf')
        visited=set()
        while True:
            safety, r, c = heapq.heappop(h)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            res=min(res, -safety)
            if (r,c)==(n-1,n-1):
                return res
            for dr,dc in neighbors:
                if dr+r<0 or dr+r>=n or dc+c<0 or dc+c>=n:
                    continue
                heapq.heappush(h, (-scores[r+dr][c+dc],r+dr, c+dc))