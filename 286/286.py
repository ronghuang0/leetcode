# 286. Walls and Gates

# bfs
# time: O(mn) space: O(mn)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms):
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row,col))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r+dr
                nc = c+dc
                if 0<=nr<m and 0<=nc<n and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c]+1
                    q.append((nr,nc))