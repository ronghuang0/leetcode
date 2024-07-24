# 2093. Minimum Cost to Reach City With Discounts

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj=defaultdict(list)
        for u,v,w in highways:
            adj[u].append((v,w))
            adj[v].append((u,w))
        h=[(0, 0, 0)] #curr distance, curr discounts taken, node
        dp={} #(node, d)
        while h:
            path, d, node = heapq.heappop(h)
            
            if d>discounts:
                continue
            if (node, d) in dp and path>=dp[(node,d)]:
                continue
            dp[(node,d)]=path
            if node==n-1:
                return path
            for v,w in adj[node]:
                heapq.heappush(h,(path+w,d,v))
                heapq.heappush(h,(path+w//2, d+1, v))
        return -1
