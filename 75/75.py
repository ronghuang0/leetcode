# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        m=0
        while m<=r:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                m+=1
                l+=1
            elif nums[m]==2:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
            else:
                m+=1
            

        