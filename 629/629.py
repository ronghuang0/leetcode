# 629. K Inverse Pairs Array

# recursion, O(n*k) space and time
from functools import cache
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(num, count):
            if count == 0:
                return 1
            if count < 0:
                return 0
            if num <= 0:
                return 0
            total = 0
            total += dfs(num, count-1)+dfs(num-1,count)-dfs(num-1, count-1-num)
            total %= mod
            return total
        return dfs(n-1,k)
    
# tabulation, time: O(n*k) space: O(k)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        prev = [0]*(k+1)
        prev[0] = 1
        for i in range(1, n+1):
            curr = [0]*(k+1)
            total = 0
            for j in range(0, k+1):
                if j >= i:
                    total-=prev[j-i]
                total = (total+prev[j])%mod
                curr[j] = total
            prev = curr
        return prev[k]
               