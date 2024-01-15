# 2225. Find Players With Zero or One Losses

# O(nlogn) time and  O(n) space
class Solution:
    def findWinners(self, matches):
        zero = set()
        one = set()
        more = set()
        for w,l in matches:
            if w not in one and w not in more:
                zero.add(w)
            if l in zero:
                zero.remove(l)
                one.add(l)
            elif l in one:
                one.remove(l)
                more.add(l)
            elif l in more:
                continue
            else:
                one.add(l)
        z = list(zero)
        o = list(one)
        z.sort()
        o.sort()
        return [z, o]