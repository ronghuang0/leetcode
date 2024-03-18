# 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda x:x[1])
        currEnd = points[0][1]
        count=1
        for start,end in points:
            if start > currEnd:
                currEnd=end
                count+=1
        return count