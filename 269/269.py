#269. Alien Dictionary

# bfs: kahn's algorithm
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


# postorder dfs
    
class Solution:
    def alienOrder(self, words):
        adj = {}
        for word in words:
            for letter in word:
                if letter not in adj:
                    adj[letter] = []

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j > len(word2)-1:
                    return ''
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        res = []
        cycle = set()
        visited = set()
        def dfs(node):
            if node in visited:
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            cycle.remove(node)
            res.append(node)
            visited.add(node)
            return True
        
        for n in adj:
            if not dfs(n):
                return ''
        res.reverse()
        return ''.join(res)