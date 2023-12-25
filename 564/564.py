# 564. Find the Closest Palindrome

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        cand = [str(10**(k-1)-1), str(10**k+1)]
        m = (k+1)//2
        prefix = n[:m]
        p = [prefix, str(int(prefix)+1), str(int(prefix)-1)]
        for v in p:
            if k%2==0:
                cand.append(v+v[::-1])
            else:
                cand.append(v+v[:-1][::-1])
        res = float('inf')
        currD = float('inf')
        print(cand)
        for c in cand:
            d = abs(int(n)-int(c))
            if c!=n and (d < currD or (d==currD and int(c)<int(n))):
                res=c
                currD=d
        return res