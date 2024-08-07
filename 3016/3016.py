# 3016. Minimum Number of Pushes to Type Word II
class Solution:
    def minimumPushes(self, word: str) -> int:
        def convert(num):
            return (num-1)//8+1

        c = Counter(word)
        res=0
        count=0
        v = list(c.values())
        v.sort(reverse=True)
        for f in v:
            count+=1
            res+=f*convert(count)
        return res