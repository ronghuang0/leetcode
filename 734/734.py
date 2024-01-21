# 734. Network Delay Time

from collections import defaultdict
import heapq
# time:
# space:
class Solution:
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        q = [(0,k)]
        res = {}
        while(q):
            time, u = heapq.heappop(q)
            if u in res:
                continue
            res[u] = time
            if len(res) == n:
                return time
            for v, w in adj[u]:
                heapq.heappush(q, (time+w, v))
        return -1