# 274. H-Index

# O(n) counting sort
class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        count = [0]*(len(citations)+1)
        for c in citations:
            count[min(c,n)]+=1
        k = n
        sum = count[n]
        while k>sum:
            k-=1
            sum+=count[k]
        return k