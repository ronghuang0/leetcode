// my first attempt at this was TLE. instead of going row by row I had spaces array and filtered the spaces as queens were placed. This did a lot of extra
// work. Every time i added one solution we were back at zero had to recalculate.


// what is best way to make matrix in js?
// remember how .join works? how does .fill work?
// set has less than linear lookup and delete (better than array)


var solveNQueens = function(n) {
    let cols = new Set();
    let posDiag = new Set();
    let negDiag = new Set();
    let res = []

    let board = [];
    for(let i=0;i<n;i++) {
        board.push(new Array(n).fill('.'));
    }

    function dfs(row) {
        if(row === n) {
            let copy = [];
            for(let i=0;i<n;i++) {
                copy.push(board[i].join(''));
            }
            res.push(copy);
            return;
        }
        
        for(let col=0; col<n;col++) {
            if(cols.has(col) || posDiag.has(row-col) || negDiag.has(row+col)) {
                continue;
            }
            board[row][col] = 'Q';
            cols.add(col);
            posDiag.add(row-col);
            negDiag.add(row+col);
            dfs(row+1);
            board[row][col] = '.';
            cols.delete(col);
            posDiag.delete(row-col);
            negDiag.delete(row+col);
        }
    }
    dfs(0);
    return res;

};