# 787. Cheapest Flights within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        stops = [float('inf')]*n
        adj=defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        h = [(0, src, 0)] # cost, node, stops
        while h:
            price, node, s = heapq.heappop(h)
            if s >= stops[node]:
                continue
            if s > k+1:
                continue
            if node == dst:
                return price
            stops[node] = s
            for nei, p in adj[node]:
                heapq.heappush(h, (price+p, nei, s+1))
        return -1