# 276. Paint Fence

# time: O(n) space: O(1)
class Solution:
    def numWays(self, n, k):
        if n==1:
            return k
        prevPrev = k
        prev= k*k
        for i in range(3,n+1):
            curr = (k-1)*prev+(k-1)*prevPrev
            prevPrev = prev
            prev = curr
        return prev