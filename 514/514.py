# 514. Freedom Trail

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        map=defaultdict(list)
        for i,char in enumerate(ring):
            map[char].append(i)
        def getDistance(x,y):
            return min(abs(y-x), abs(len(ring)-abs(y-x)))
        # i - ring
        # j - key
        @cache
        def dfs(i, j):
            if j==len(key):
                return 0
            res=float('inf')
            for k in map[key[j]]:
                d=getDistance(i,k)
                res=min(res, d+dfs(k, j+1))
            return res
        return dfs(0,0)+len(key)

            
            