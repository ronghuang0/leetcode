# 1066. Campus Bikes II

# backtracking + early termination
# tle
class Solution:
    def __init__(self):
        self.res = float('inf')
        self.visited = [0]*10
    def getDistance(self, worker, bike):
        return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
    def assignBikes(self, workers, bikes):
        def dfs(i, currDist):
            if i == len(workers):
                self.res = min(self.res, currDist)
                return
            if currDist >= self.res:
                return
            for j in range(len(bikes)):
                if self.visited[j]:
                    continue
                self.visited[j] = 1
                dfs(i+1, currDist + self.getDistance(workers[i], bikes[j]))
                self.visited[j] = 0
        dfs(0, 0)
        return self.res


# memo + backtracking + bitmask
from functools import cache
class Solution:
    def getDistance(self, worker, bike):
        return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
    def assignBikes(self, workers, bikes):
        @cache
        def dfs(pos, b):
            if pos == len(workers):
                return 0
            ans = float('inf')
            for i in range(len(b)):
                if b[i] == '1':
                    continue
                d = self.getDistance(workers[pos],bikes[i])
                ans = min(ans, d+dfs(pos+1, b[:i]+'1'+b[i+1:]))
            return ans
        return dfs(0, ''.join(['0']*len(bikes)))