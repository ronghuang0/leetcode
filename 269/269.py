#269. Alien Dictionary

from collections import defaultdict
class Solution:
    def alienOrder(self, words):
        adj = defaultdict(list)
        indegree = {}
        letters = set()
        for word in words:
            for letter in word:
                letters.add(letter)
        for i in range(len(words)-1):
            for k in range(len(words[i])):
                if len(words[i+1])-1<k:
                    return ''
                if words[i][k] == words[i+1][k]:
                    continue
                adj[words[i][k]].append(words[i+1][k])
                if words[i][k] not in indegree:
                    indegree[words[i][k]]=0
                if words[i+1][k] not in indegree:
                    indegree[words[i+1][k]]=0
                indegree[words[i+1][k]]+=1
                break
        res = []
        s = []
        for letter, degree in indegree.items():
            if degree == 0:
                s.append(letter)
        while s:
            curr = s.pop()
            res.append(curr)
            letters.remove(curr)
            for letter in adj[curr]:
                indegree[letter]-=1
                if indegree[letter] == 0:
                    s.append(letter)
        if len(res) == len(indegree):
            return ''.join(res) + ''.join(list(letters))
        return ''
