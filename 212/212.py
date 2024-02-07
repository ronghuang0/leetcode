# 212. Word Search II

class TreeNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TreeNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TreeNode()
            curr = curr.children[c]
        curr.word = word
    
class Solution:
    def findWords(self, board, words):
        self.tree = Trie()
        for w in words:
            self.tree.insert(w)
        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        res = set()
        visited = set()
        def dfs(point, parent):
            if point in visited:
                return
            visited.add(point)
            r, c = point
            node = parent.children[board[r][c]]
            if node.word:
                res.add(node.word)
            if len(node.children) == 0:
                del parent.children[board[r][c]]
            for dr, dc in dirs:
                nr = r+dr
                nc = c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                if board[nr][nc] in node.children:
                    dfs((nr,nc), node)
            visited.remove(point)
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.tree.root.children:
                    dfs((i,j), self.tree.root)
        return res