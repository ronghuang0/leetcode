# 1649. Create Sorted Array through Instructions

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9+7
        m = max(instructions)
        bit = [0]*(m+1)

        def update(i):
            while i<len(bit):
                bit[i]+=1
                lsb = i&-i
                i = i+lsb
        def get(i): #prefix sum including i
            res = 0
            while i>0:
                res+=bit[i]
                lsb = i&-i
                i = i-lsb
            return res
        cost = 0
        for i, num in enumerate(instructions):
            # when we are at index i there are already i elements in array
            cost += min(get(num-1), i-get(num))
            update(num)
        return cost % mod