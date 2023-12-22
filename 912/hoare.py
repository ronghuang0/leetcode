# hoare
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l,r):
            pivot = nums[l]
            l = l-1
            r = r+1
            while True:
                l+=1
                while nums[l]<pivot:
                    l+=1
                r-=1
                while nums[r]>pivot:
                    r-=1
                if l>=r:
                    return r
                nums[l], nums[r] = nums[r], nums[l]
        
        def sort(l, r):
            if(l>=r):
                return
            pivot = partition(l,r)
            sort(l, pivot)
            sort(pivot+1, r)
        
        sort(0, len(nums)-1)
        return nums