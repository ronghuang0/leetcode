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

# O(n) space. Not in place, but helps with repeating numbers
# average O(n) time complexity. n+n/2+n/4+...
# worst case O(n^2) time complexity

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr):
            pivot=arr[0]
            left,mid,right=[],[],[]
            for a in arr:
                if a<pivot:
                    left.append(a)
                elif a>pivot:
                    right.append(a)
                else:
                    mid.append(a)
            return (left, mid, right)
          
        def find(arr, j):
            l,m,r = partition(arr)
            if j<=len(r):
                return find(r, j)
            if j>len(r)+len(m):
                return find(l,j-len(r)-len(m))
            return m[0]
        
        return find(nums,k)
