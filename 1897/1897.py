# 1897. Redistribute Characters to Make All Strings Equal

from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        map = defaultdict(int)
        for s in words:
            for c in s:
                map[c]+=1
        for n in map.values():
            if n % len(words) != 0:
                return False
        return True