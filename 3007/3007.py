# Weekly Contest 380 q3
# 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K

# For a value num, for the range 1 to num, we can find the number of the 1s for each bit i
# 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
# notice for bit 0 the length of a sequence is 2, 1->4, 2->8, 3->16 S=2^i
# we can find number of complete sequences with (num+1)/S, multiplied by S/2 is 1s
# we can find remainder with (num+1)%S. since each sequence starts with 0, we can do (num+1)%S - S/2
import math
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
