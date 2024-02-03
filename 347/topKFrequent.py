# 347. Top K Frequent Elements

# hash map and sort
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        dict = defaultdict(int)
        for n in nums:
            dict[n]+=1
        list = []
        for key, value in dict.items():
            list.append((value, key))
        list.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(list[i][1])
        return res
    
# bucket sort
from collections import Counter 
class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in c.items():
            bucket[value].append(key)
        res = []
        index = len(bucket)-1
        while len(res) < k:
            while len(bucket[index]) == 0:
                index-=1
            res.append(bucket[index].pop())
        return res
    
# heap
import heapq 
class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        arr=[]
        for key, value in c.items():
            arr.append((-value, key))
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res
    
# quick select
# time: O(n), O(n^2) worst case
# space: O(n)
class Solution:
    def topKFrequent(self, nums, k: int):
        c = Counter(nums)
        values = list(c.keys())
        def partition(start, end):
            pivot = c[values[end]]
            left = start
            for right in range(start, end):
                if c[values[right]] <= pivot:
                    values[left], values[right] = values[right], values[left]
                    left+=1
            values[left], values[end] = values[end], values[left]
            return left
        
        def select(start, end):
            pivotIndex = partition(start, end)
            if pivotIndex == len(values)-k:
                return
            elif pivotIndex > len(values)-k:
                select(start, pivotIndex-1)
            else:
                select(pivotIndex+1, end)
        select(0, len(values)-1)
        return values[len(values)-k:]

        

