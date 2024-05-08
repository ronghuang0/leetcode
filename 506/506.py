# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        ss=sorted(score, reverse=True)
        map={}
        for i in range(n):
            map[ss[i]]=i

        res = []
        for s in score:
            if map[s]==0:
                res.append('Gold Medal')
            elif map[s]==1:
                res.append('Silver Medal')
            elif map[s]==2:
                res.append('Bronze Medal')
            else:
                res.append(str(map[s]+1))
        return res