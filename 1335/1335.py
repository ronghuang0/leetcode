# 1335. Minimum Difficulty of a Job Schedule

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        l = len(jobDifficulty)
        @cache
        def dfs(daysLeft, currMax, index):
            if index == l and daysLeft > 0:
                return float('inf')
            if daysLeft==0:
                return max([currMax] + jobDifficulty[index:])
            sameDay = dfs(daysLeft, max(currMax, jobDifficulty[index]), index+1)
            nextDay = currMax+dfs(daysLeft-1, jobDifficulty[index], index+1)
            return min(sameDay, nextDay)
        res = dfs(d-1, jobDifficulty[0], 1)
        if res == float('inf'):
            return -1
        return res
