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

# 2d dp
# index represents index of first task for that day
# daysLeft is number of days left

from functools import cache
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        l = len(jobDifficulty)
        if d > l:
            return -1
        @cache
        def dfs(index, daysLeft):
            if index == l:
                if daysLeft == 0:
                    return 0
                return float('inf')
            if daysLeft == 0:
                return float('inf')
            ans = float('inf')
            biggestJob = 0
            for i in range(index+1, l+1):
                biggestJob = max(biggestJob, jobDifficulty[i-1])
                ans = min(ans, biggestJob+dfs(i, daysLeft-1))
            return ans
        return dfs(0,d)
    
# bottom up 2d
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        l = len(jobDifficulty)
        if d > l:
            return -1
        dp = [[float('inf')]*(l+1) for __ in range(d+1)]
        dp[0][l] = 0
        for i in range(1, d+1):
            for j in range(l+1):
                ans = float('inf')
                biggestJob = 0
                for x in range(j+1, l+1):
                    biggestJob = max(biggestJob, jobDifficulty[x-1])
                    ans = min(ans, biggestJob + dp[i-1][x])
                dp[i][j] = ans
        return dp[d][0]

# bottom up 1d
class Solution:
    def minDifficulty(self, jobDifficulty, d: int):
        l = len(jobDifficulty)
        if d > l:
            return -1
        prev = [float('inf')]*(l+1)
        prev[l] = 0
        for i in range(1, d+1):
            curr = [0]*(l+1)
            for j in range(l+1):
                ans = float('inf')
                biggestJob = 0
                for x in range(j+1, l+1):
                    biggestJob = max(biggestJob, jobDifficulty[x-1])
                    ans = min(ans, biggestJob + prev[x])
                curr[j] = ans
            prev = curr
        return prev[0]

# monotonic stack optimization - The key insight is that after extending the job schedule that ends at index j once, we never need to consider extending it again.
# think of day as day we are on
# think of index as last job for day we are on
# dp[d][i] is min total difficulty so far for day d ending on job i
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        l = len(jobDifficulty)
        if d > l:
            return -1
        prev_day = [float('inf')]*l
        for day in range(d):
            stack = []
            curr_day = [float('inf')]*l
            for i in range(day, l):
                if i==0:
                    curr_day[0] = jobDifficulty[0]
                else:
                    curr_day[i] = prev_day[i-1]+jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    curr_day[i] = min(curr_day[i], curr_day[j]+jobDifficulty[i]-jobDifficulty[j])
                if stack:
                    curr_day[i] = min(curr_day[i], curr_day[stack[-1]])
                stack.append(i)
            prev_day = curr_day
        return prev_day[-1]