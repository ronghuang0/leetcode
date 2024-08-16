# 624. Maximum Distance in Arrays

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest=float('inf')
        biggest=float('-inf')
        res=0
        for a in arrays:
            res=max(res, a[-1]-smallest, biggest-a[0])
            smallest=min(smallest, a[0])
            biggest=max(biggest, a[-1])
        return res