# 1657. Determine if Two Strings Are Close

# hashmap 
# time: O(n)  space: O(1) - length of 26
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
    
# arrays
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1=[0]*26
        freq2=[0]*26
        for c in word1:
            freq1[ord(c)-ord('a')]+=1
        for c in word2:
            freq2[ord(c)-ord('a')]+=1
        for i in range(len(freq1)):
            if (freq1[i] == 0 and freq2[i] > 0) or (freq2[i] == 0 and freq1[i] >0):
                return False
        freq1.sort()
        freq2.sort()
        return freq1==freq2