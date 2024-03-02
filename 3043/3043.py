# 3043. Find the Length of the Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = {}
        for n in arr1:
            for i in range(len(str(n))):
                prefixes[str(n)[:i+1]]=True
        res = 0
        for n in arr2:
            for i in range(len(str(n))):
                p = str(n)[:i+1]
                if p in prefixes:
                    res = max(res, len(p))
        return res
    
class Node:
    def __init__(self, val):
        self.isWord = val
        self.children = {}
class Trie:
    def __init__(self):
        self.head = Node(False)
    def add(self, word):
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(False)
            curr = curr.children[char]
        curr.isWord = True
    def prefix(self, word):
        curr = self.head
        count = 0
        for char in word:
            if char in curr.children:
                count+=1
            else:
                break
            curr = curr.children[char]
        return count
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for a in arr1:
            t.add(str(a))
        res = 0
        for b in arr2:
            res=max(res, t.prefix(str(b)))
        return res