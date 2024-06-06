# 846. Hand of Straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        hand.sort()
        # 1 2 2 3 3 4 5 6 7
        freq = Counter(hand)
        while len(freq):
            first = next(iter(freq))
            for i in range(first, first+groupSize):
                if i in freq and freq[i]>0:
                    freq[i]-=1
                    if freq[i]==0:
                        del freq[i]
                else:
                    return False
        return True
    
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        freq=Counter(hand)
        h=list(freq.keys())
        heapq.heapify(h)
        while h:
            start=h[0]
            for i in range(groupSize):
                if freq[start+i]==0:
                    return False
                freq[start+i]-=1
                if freq[start+i]==0:
                    if heapq.heappop(h)!=(start+i):
                        return False
        return True