# 57 Insert Intervals

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        newStart, newEnd = newInterval
        res=[]
        while i<len(intervals) and intervals[i][1]<newStart:
            res.append(intervals[i])
            i+=1
        while i<len(intervals) and intervals[i][0]<=newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i+=1
        res.append([newStart, newEnd])
        res+=intervals[i:]
        return res