# 28. Find the Index of the First Occurence in a String

# knuth-morris-pratt
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0]*len(needle)
        i=0
        j=1
        while j<len(needle):
            if needle[i] == needle[j]:
                i+=1
                lps[j]=i
                j+=1
            elif i==0:
                j+=1
            else:
                i=lps[i-1]
        i=0
        j=0
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == len(needle):
                    return i-j
            elif j==0:
                i+=1
            else:
                j=lps[j-1]
        return -1