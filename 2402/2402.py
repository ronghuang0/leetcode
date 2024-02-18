# 2402. Meeting Rooms III

import heapq
class Solution:
    def mostBooked(self, n: int, meetings) -> int:
        meetings.sort(key=lambda a:a[0])
        res = [0]*n
        h = []
        avail = [i for i in range(0, n)]
        heapq.heapify(avail)
        for m in meetings:
            start, end = m
            while h and h[0][0]<=start:
                e, room = heapq.heappop(h)
                heapq.heappush(avail, room)
            if avail:
                r = heapq.heappop(avail)
                res[r]+=1
                heapq.heappush(h, (end,r))
            else:
                e, room = heapq.heappop(h)
                heapq.heappush(h, (end-start+e, room))
                res[room]+=1
        ans = 0
        most = 0
        for i in range(len(res)):
            if res[i]>most:
                ans = i
                most = res[i]
        return ans