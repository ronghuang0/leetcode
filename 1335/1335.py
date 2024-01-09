# 1335. Minimum Difficulty of a Job Schedule

# 3d dp
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        l = len(jobDifficulty)
        if d > l:
            return -1
        cache = {}
        def dfs(index, currMax, daysLeft):
            if index == l and daysLeft > 0:
                return float('inf')
            if daysLeft==0:
                return max([currMax] + jobDifficulty[index:])
            if (index, currMax, daysLeft) in cache:
                return cache[(index, currMax, daysLeft)]
            sameDay = dfs(index+1, max(currMax, jobDifficulty[index]), daysLeft)
            nextDay = currMax+dfs(index+1, jobDifficulty[index], daysLeft-1)
            cache[(index, currMax, daysLeft)] = min(sameDay, nextDay)
            return cache[(index, currMax, daysLeft)]
        return dfs(1, jobDifficulty[0], d-1)
    
# same logic, just with different base case
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        if d>len(jobDifficulty):
            return -1
        cache = {}
        def dfs(index, currMax, daysLeft):
            if index == len(jobDifficulty):
                return 0 if daysLeft == 0 else float('inf')
            if daysLeft == 0:
                return float('inf')
            if (index, currMax, daysLeft) in cache:
                return cache[(index, currMax, daysLeft)]  
            sameDay = dfs(index+1, max(currMax, jobDifficulty[index]), daysLeft)
            nextDay = max(currMax, jobDifficulty[index])+dfs(index+1, -1, daysLeft-1)
            cache[(index, currMax, daysLeft)] = min(sameDay, nextDay)
            return cache[(index, currMax, daysLeft)] 
        return dfs(0, -1, d)

#2d dp
    