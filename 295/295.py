# 295. Find Median from Data Stream

import heapq

# time: O(log(n)) for each addNum
# space: O(n)
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        val = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, val)
        if len(self.maxHeap) < len(self.minHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)   

    def findMedian(self) -> float:
        if (len(self.maxHeap)+len(self.minHeap))%2 == 0:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        else:
            return -self.maxHeap[0]
