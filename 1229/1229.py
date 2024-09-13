# 1229. Meeting Scheduler

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        c=list(filter(lambda x: x[1]-x[0]>=duration, slots1+slots2))
        c.sort(key=lambda x:x[0])
        res=[]
        for i in range(len(c)-1):
            s1,e1=c[i]
            s2,e2=c[i+1]
            if e1-s2>=duration:
                return [s2, s2+duration]
        return []
        
        