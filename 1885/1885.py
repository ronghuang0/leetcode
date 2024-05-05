# 1885. Count Pairs in Two Arrays

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i]-nums2[i] +nums1[j]-nums2[j]>0
        n=len(nums1)
        diff = []
        for i in range(n):
            diff.append(nums1[i]-nums2[i])
        diff.sort()
        l=0
        r=n-1
        res=0
        while l<r:
            if (diff[l]+diff[r])<=0:
                l+=1
            else:
                res+=r-l
                r-=1
        return res