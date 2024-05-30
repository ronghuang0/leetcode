# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0]
        s=0
        for i in range(n):
            s^=arr[i]
            prefix.append(s)
        res=0
        for i in range(n+1):
            for j in range(i+1,n+1):
                if (prefix[j]-prefix[i])==0:
                    res+=j-i-1
        return res