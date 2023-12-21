# 347. Top K Frequent Elements

# hash map and sort
from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr=[]
        for key, value in c.items():
            arr.append((-value, key))
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res

        

