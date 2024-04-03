# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        seen=set()
        def dfs(i, r, c):
            if r==m or c==n or r<0 or c<0:
                return False
            if (r,c) in seen:
                return False
            if board[r][c] != word[i]:
                return False
            seen.add((r,c))
            if len(seen)==len(word):
                return True
            neigh = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]
            for nr,nc in neigh:
                if dfs(i+1, nr, nc):
                    return True
            seen.remove((r,c))
            return False
                    
        for r in range(m):
            for c in range(n):
                if dfs(0, r,c):
                    return True
        return False