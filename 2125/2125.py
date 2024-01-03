# 2125. Number of Laser Beams in a Bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for b in bank:
            s = sum(map(int, b))
            if s>0:
                ans+=s*prev
                prev = s
        return ans