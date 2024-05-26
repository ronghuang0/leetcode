# 3164.

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        fn2=defaultdict(int)
        for n in nums2:
            fn2[n]+=1
        count=0
        @cache
        def getFactors(n):
            c=0
            for i in range(1,math.floor(math.sqrt(n))+1):
                if n%i==0:
                    if i%k==0:
                        c+=fn2[i//k]
                    if n//i!=i and (n//i)%k==0:
                        c+=fn2[(n//i)//k]
            return c
        for n in nums1:
            count+=getFactors(n)
        return count

        
        