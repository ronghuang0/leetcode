# 1155. Number of Dice Rolls With Target Sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(remain, sum):
            if sum > target:
                return 0
            if remain == 0:
                if sum==target:
                    return 1
                return 0
            res = 0
            for i in range(1, k+1):
                res= (res + dfs(remain-1, sum+i)%mod)%mod
            return res
        return dfs(n, 0)
    
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod=10**9+7
        dp=[[0]*(target+1)]*(n+1)
        dp[0][target] = 1
        for i in range(1, n+1):
            for j in range(0, target+1):
                res = 0
                for x in range(1, k+1):
                    if j+x <= target:
                        res= (res+dp[i-1][j+x]%mod)%mod
                dp[i][j]=res
        return dp[n][0]
    
# space optimized

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod=10**9+7
        prev = [0]*(target+1)
        prev[target]=1
        for i in range(1, n+1):
            curr = [0]*(target+1)
            for j in range(0, target+1):
                res = 0
                for x in range(1, k+1):
                    if j+x <= target:
                        res= (res+prev[j+x]%mod)%mod
                curr[j]=res
            prev = curr
        return curr[0]
