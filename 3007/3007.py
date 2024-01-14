# Weekly Contest 380 q3
# 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def findSum(num):
            num +=1
            total = 0
            for i in range(62):
                if (i+1)%x != 0:
                    continue
                size = 1<<(i+1)
                blocks = num//size
                leftover = num % size
                total += blocks*size/2 + max(0, leftover-size/2)
            return total
        l=0
        r=10**20
        while l<r:
            mid = math.ceil((l+r)/2)
            if findSum(mid) <= k:
                l = mid
            else:
                r = mid-1
        return l
