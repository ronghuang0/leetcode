# 1851. Minimum Interval to Include Each Query

# time: O(nlogn) space: O(n)
import heapq
class Solution:
    def minInterval(self, intervals, queries):
        res = {}
        intervals.sort(reverse=True)
        h = []
        for q in sorted(queries):
            while intervals and  q >= intervals[-1][0]:
                s, e = intervals.pop()
                heapq.heappush(h, [e-s+1, e])
            while h and q > h[0][1]:
                heapq.heappop(h)
            if h:
                res[q] = h[0][0]
            else:
                res[q] = -1
        arr = []
        for n in queries:
            arr.append(res[n])
        return arr