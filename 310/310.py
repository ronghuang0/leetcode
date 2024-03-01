# 310. Minimum Height Trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        leaves = []
        for i in range(len(indegree)):
            if indegree[i] == 1:
                leaves.append(i)
        nodesLeft = set([i for i in range(n)])
        while len(nodesLeft)>2:
            next = []
            print(leaves)
            for leaf in leaves:
                nodesLeft.discard(leaf)
                for nei in adj[leaf]:
                    indegree[nei]-=1
                    if indegree[nei] == 1:
                        next.append(nei)
            leaves=next
        return list(nodesLeft)