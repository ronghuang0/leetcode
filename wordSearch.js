

// time complexity: O(m*n*3^s) where s is the length of the word. 3 because each dfs has 3 neighbors not counting the one we just came from.
// i dont think it's even possible to have an example where we get 3^s because we run out of space right away and in order to get the full time we
// need the letters to continue making the word which is impossible... but this is what everyone says and i dont know how to calculate it closer
// okay - i thought of an example, if our words was 'AAAAAAAAAA....' and our board was all As this would be close to the worst case. The only thing
// stopping it would be the visited parts but for a big board i think it would be closer to correct.



// dfs every neighbor vs checking the bounds of the neighbors and dfs that
// if you just dfs every neighbor then it takes care of the edge case of board = [[a]] and word = 'a'


var exist = function(board, word) {
    const ROWS = board.length;
    const COLS = board[0].length;
    let visited = {};
    function dfs(row, col, i) {
        if(i === word.length) {
            return true
        }
        if(row<0 || row >= ROWS || col<0 || col>=COLS || visited[`${row}_${col}`] || word[i] !== board[row][col]){
            return false;
        }
        visited[`${row}_${col}`] = 1;
        res = dfs(row+1, col, i+1) || dfs(row-1, col, i+1) || dfs(row, col+1, i+1) || dfs(row, col-1, i+1);
        visited[`${row}_${col}`] = 0;
        return res;
    }
    for(let i=0; i<ROWS; i++) {
        for(let j=0; j<COLS; j++) {
            let res = dfs(i, j, 0);
            if(res) return res;
        }
    }
    return false;
}

