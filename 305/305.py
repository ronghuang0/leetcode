# 305. Number of Islands II

class DSU():
    def __init__(self, length):
        self.parent=[-1]*length
        self.rank=[1]*length
        self.count=0
    def addLand(self, a):
        if self.parent[a]!=-1:
            return
        self.count+=1
        self.parent[a]=a
    def isLand(self, a):
        return self.parent[a] != -1
    def find(self, a):
        if self.parent[a]==a:
            return a 
        self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa==pb:
            return
        if self.rank[pa]>=self.rank[pb]:
            self.parent[pb]=self.parent[pa]
            self.rank[pa]+=self.rank[pb]
        else:
            self.parent[pa]=self.parent[pb]
            self.rank[pb]+=self.rank[pa]
        self.count-=1
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        d = DSU(m*n)
        res=[]
        for r, c in positions:
            pos = r*n+c
            nei = [(r+1, c), (r-1,c), (r,c+1),(r,c-1)]
            d.addLand(pos)
            for nr, nc in nei:
                npos = nr*n+nc
                if nr<0 or nr>=m or nc<0 or nc>=n or not d.isLand(npos):
                    continue
                d.union(pos, npos)
            res.append(d.count)
        
        return res


    