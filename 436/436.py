# 436. Find Right Interval

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        map={}
        for i, val in enumerate(intervals):
            map[val[0]]=i
        sortedIntervals = sorted(intervals, key=lambda x:x[0])
        res=[]
        for start,end in intervals:
            l=0
            r=len(intervals)-1
            while l<r:
                mid=(l+r)//2
                if sortedIntervals[mid][0]<end:
                    l=mid+1
                else:
                    r=mid
            if sortedIntervals[l][0] < end:
                res.append(-1)
            else:
                res.append(map[sortedIntervals[l][0]])
        return res
            
