# 981. Time Based Key-value Store
class TimeMap:
    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        map=self.map
        if key in map:
            l=0
            r=len(map[key])-1
            while l<r:
                mid = (l+r+1)//2
                if map[key][mid][0] <= timestamp:
                    l=mid
                else:
                    r=mid-1
            if map[key][l][0] > timestamp:
                return ''
            return map[key][l][1]
        return ''
