# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        res=0
        while l<r:
            leftMax=max(leftMax, height[l])
            rightMax=max(rightMax,height[r])
            if leftMax<=rightMax:
                res+=max(leftMax-height[l],0)
                l+=1
            else:
                res+=max(rightMax-height[r],0)
                r-=1
        return res