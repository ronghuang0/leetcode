# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = set()
        map={}
        for i, val in enumerate(s):
            if val in map:
                if map[val] != t[i]:
                    return False
            else:
                if t[i] in seen:
                    return False
                map[val]=t[i]
                seen.add(t[i])
        return True