# 51. N-Queens
class Solution:
    def solveNQueens(self, n: int):
        rows = set()
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [['.']*n for _ in range(n)]
        res = set()
        def dfs(i):
            if i == n:
                copy = []
                for r in board:
                    copy.append(''.join(r))
                res.add(tuple(copy))
                return
            for j in range(n):
                if i in rows or j in cols or (i-j) in diag1 or (i+j) in diag2:
                    continue
                rows.add(i)
                cols.add(j)
                diag1.add(i-j)
                diag2.add(i+j)
                board[i][j] = 'Q'
                dfs(i+1)
                board[i][j] = '.'
                rows.remove(i)
                cols.remove(j)
                diag1.remove(i-j)
                diag2.remove(i+j)
        dfs(0)
        return res