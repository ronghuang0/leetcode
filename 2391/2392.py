# 2392. Build a Matrix with Conditions

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def getTop(n, edges):
            adj=defaultdict(list)
            indegree=[0]*(n+1)

            for u,v in edges:
                adj[u].append(v)
                indegree[v]+=1
            z=deque()
            for i in range(1,n+1):
                if indegree[i]==0:
                    z.append(i)
            res=[]
            while z:
                curr = z.pop()
                res.append(curr)
                for nei in adj[curr]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        z.appendleft(nei)
            if len(res)==n:
                return res
            return []
        r = getTop(k, rowConditions)
        c = getTop(k, colConditions)
        if not r or not c:
            return []
        mat = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if r[i]==c[j]:
                    mat[i][j]=r[i]
        return mat
