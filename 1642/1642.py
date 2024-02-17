# 1642. Furthest Building You Can Reach

import heapq
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        h = []
        for i in range(1, len(heights)):
            curr = heights[i]-heights[i-1]
            if curr<=0:
                continue
            if ladders !=0:
                heapq.heappush(h, curr)
                ladders-=1
                continue
            if h and heights[i] > h[0]:
                heapq.heappush(h, curr)
                curr = heapq.heappop(h)
            if curr<=bricks:
                bricks-=curr
            else:
                return i-1
        return len(heights)-1