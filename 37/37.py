# 37. Sudoku Solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            if row==9:
                return True
            if col==9:
                return dfs(row+1, 0)
            if board[row][col]!='.':
                return dfs(row, col+1)
            sq=(row//3)*3+col//3
            for num in range(1,10):
                if  num in square[sq] or num in rows[row] or num in cols[col]:
                    continue
                square[sq].add(num)
                rows[row].add(num)
                cols[col].add(num)
                board[row][col]=str(num)
                if dfs(row, col+1):
                    return True
                square[sq].remove(num)
                rows[row].remove(num)
                cols[col].remove(num)
                board[row][col]='.'
        
        square=defaultdict(set)
        rows=defaultdict(set)
        cols=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    sq=(i//3*3)+j//3
                    square[sq].add(int(board[i][j]))
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
        dfs(0,0)