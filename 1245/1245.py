#1245. Tree Diameter

from collections import defaultdict

# two dfs calls
class Solution:
    def treeDiameter(self, edges):
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node, visited):
            length = -1
            target = node
            for e in adj[node]:
                if e in visited:
                    continue
                visited.add(e)
                nl, nt = dfs(e, visited)
                if nl>length:
                    length = nl
                    target = nt
            return [1+length, target]
        length, node = dfs(0, set({0}))
        resLength, resNode = dfs(node, set({node}))
        return resLength

# dfs with heights
class Solution:
    def treeDiameter(self, edges) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        res = 0
        def dfs(node, parent):
            longest = -1
            secondLongest = -1
            for nei in adj[node]:
                if nei == parent:
                    continue
                length = dfs(nei, node)
                if length > longest:
                    secondLongest = longest
                    longest = length
                elif length > secondLongest:
                    secondLongest = length
            nonlocal res
            res = max(res, longest+secondLongest+2)
            return longest+1
        dfs(0, -1)
        return res  