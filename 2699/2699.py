# 2699. Modify Graph Edge Weights
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj=defaultdict(list)
        for u,v,w in edges:
            if w!=-1:
                adj[u].append((v, w))
                adj[v].append((u, w))
        def dijkstra():
            h=[(0, source)]
            visited=set()
            while h:
                dist, node = heapq.heappop(h)
                if node in visited:
                    continue
                visited.add(node)
                if node == destination:
                    return dist
                for v, w in adj[node]:
                    heapq.heappush(h, (dist+w, v))
            return 2*10**9
        
        match=False
        path = dijkstra()
        if path<target:
            return []
        if path==target:
            match=True
        for edge in edges:
            if edge[2]!=-1:
                continue
            if match:
                edge[2]=2*10**9
                continue
            edge[2]=1
            adj[edge[0]].append((edge[1], 1))
            adj[edge[1]].append((edge[0], 1))
            path = dijkstra()
            if path<=target:
                match=True
                edge[2]+=target-path
        if match:
            return edges
        return []