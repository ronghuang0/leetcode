# 215. Kth Largest Element in an Array

# heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x:-x, nums))
        heapq.heapify(nums)
        ans = None
        for i in range(k):
            ans=heapq.heappop(nums)
        return -ans


# quick select
# this tle for 1 test case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start,end,arr):
            pivot = arr[end]
            left = start
            for right in range(start, end):
                if arr[right] <= pivot:
                    arr[left], arr[right] = arr[right], arr[left]
                    left+=1
            arr[left], arr[end] = arr[end], arr[left]
            return left
        s=0
        e=len(nums)-1
        while True:
            p = partition(s,e,nums)
            if p==len(nums)-k:
                return nums[p]
            if p<len(nums)-k:
                s=p+1
            else:
                e=p-1
