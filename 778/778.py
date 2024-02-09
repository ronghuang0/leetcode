# 778. Swim in Rising Water

# time: O(n^2logn)
# space: O(n^2)
import heapq
class Solution:
    def swimInWater(self, grid):
        m = len(grid)
        n = len(grid[0])
        h = []
        h = [(grid[0][0], (0,0), grid[0][0])]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        visited.add((0,0))
        while h:
            val, point, path = heapq.heappop(h)
            visited.add(point)
            if point == (m-1, n-1):
                return path
            r, c = point
            for dr, dc in dirs:
                nr = dr+r
                nc = dc+c
                if nr<0 or nr>=m or nc<0 or nc>=n or (nr,nc) in visited:
                    continue
                heapq.heappush(h, (grid[nr][nc], (nr,nc), max(path, grid[nr][nc])))