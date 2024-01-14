# 1657. Determine if Two Strings Are Close
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        if set(c1) != set(c2):
            return False
        f1 = list(c1.values())
        f2 = list(c2.values())
        f1.sort()
        f2.sort()
        return f1 == f2