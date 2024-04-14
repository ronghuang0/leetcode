#84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we have N rectangles to compare - each bar gets a turn
        # being the length
        res=0
        stack=[(-1,0)] #(index, height)
        for i, h in enumerate(heights):
            while len(stack)>1 and h<stack[-1][1]:
                index, height = stack.pop()
                start = stack[-1][0]+1
                end = i-1
                res=max(res, (end-start+1)*height)
            stack.append((i,h))
        end=len(heights)-1
        while len(stack)>1:
            index, height = stack.pop()
            start = stack[-1][0]+1
            res=max(res, (end-start+1)*height)
        return res