#1245. Tree Diameter

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