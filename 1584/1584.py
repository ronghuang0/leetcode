# 1584. Min Cost to Connect All Points

# prims
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        h.append((0, 0)) # distance, node
        connected = set()
        res = 0
        while len(connected) < len(points):
            distance, node = heapq.heappop(h)
            if node in connected:
                continue
            connected.add(node)
            res+=distance
            cx, cy = points[node]
            for i in range(len(points)):
                if i not in connected:
                    x,y=points[i]
                    heapq.heappush(h,(abs(x-cx)+abs(y-cy), i))
        return res      