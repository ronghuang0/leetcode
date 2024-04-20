// first draft  ---  i made a set of all squares to visit and removed from that set when visisted, and took from that set when queue was empty
// doing bfs on every square and keeping track of visited is easier... also, getting a single value from a set is annoying and not really wat
// a set is made for. in js we need an iterator. also - javascript sets cant handle tuples because it stores the reference and there isn't a 
// great way to do it. Handling string conversion is annoying.....

var numIslands = function(grid) {
    let count = 0;
    let ones = new Set();
    let queue = [];
    let ROWS = grid.length;
    let COLS = grid[0].length

    for(let i =0; i<ROWS;i++) {
        for(let j=0; j<COLS; j++) {
            if(grid[i][j] === '1'){
                ones.add(`${i}_${j}`);
            } 
        }
    }
    while(ones.size) {
        let str = ones.values().next().value;
        ones.delete(str);
        // 'i_j'
        // at first i used str[0] and str[2] which was dumb cuz double digits
        let [i, j] = str.split('_');
        queue.push([i, j]);
        let dir = [[0,1], [1,0], [-1,0], [0,-1]]; 
        while(queue.length) {
            let [r, c] = queue.pop();
            ones.delete(`${r}_${c}`);
            for(let [dr, dc] of dir) {
                let nr = Number(r)+dr;   // definitely forgot to use Number
                let nc = Number(c)+dc;
                // used ones[] insteaad of ones.has()
                if(nr >=0 && nr < ROWS && nc >= 0 && nc < COLS && ones.has(`${nr}_${nc}`) && grid[nr][nc] === '1') {
                    
                    
                    queue.push([nr, nc]);
                }
            }
        }
        count++;
    }
    return count;
};


// better version
var numIslands = function(grid) {
    let count = 0;
    let visited = new Set();
    let rows = grid.length;
    let cols = grid[0].length

    let bfs = (r, c)=>{
        let queue = [[r,c]];
        visited.add(`${r}_${c}`);
        let dir = [[0,1], [1,0], [-1,0], [0,-1]]; 
        while(queue.length) {
            let [r, c] = queue.pop();
            for(let [dr, dc] of dir) {
                let nr = r+dr;  
                let nc = c+dc;
                if(nr >=0 && nr < rows && nc >= 0 && nc < cols && !visited.has(`${nr}_${nc}`) && grid[nr][nc] === '1') {
                    queue.push([nr, nc]);
                    visited.add(`${nr}_${nc}`); // it still works if we dont have this one and instead put it after queue.pop but this is slightly faster and makes more sense i think
                }
            }
        }
    }
    for(let i=0; i<rows; i++) {
        for(let j=0; j<cols; j++) {
            if(grid[i][j] === '1' && !visited.has(`${i}_${j}`)) {
                bfs(i, j);
                count++;
            }
        }
    }
    return count;
};


// changing grid to zero rather than making a new visit set
var numIslands = function(grid) {
    let count = 0;
    let visited = new Set();
    let rows = grid.length;
    let cols = grid[0].length

    let bfs = (r, c)=>{
        let queue = [[r,c]];
        let dir = [[0,1], [1,0], [-1,0], [0,-1]]; 
        while(queue.length) {
            let [r, c] = queue.pop();
            for(let [dr, dc] of dir) {
                let nr = r+dr;  
                let nc = c+dc;
                if(nr >=0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === '1') {
                    queue.push([nr, nc]);
                    grid[nr][nc] = '0';
                }
            }
        }
    }
    for(let i=0; i<rows; i++) {
        for(let j=0; j<cols; j++) {
            if(grid[i][j] === '1') {
                bfs(i, j);
                count++;
            }
        }
    }
    return count;
};


//dfs - no queue so less space

var numIslands = function(grid) {
    let rows = grid.length;
    let cols = grid[0].length;
    let count = 0;

    var dfs=(r, c) =>{
        if(r<0 || r>=rows || c<0 || c>=cols || grid[r][c] === '0') {
            return;
        }
        grid[r][c] = '0';
        dfs(r+1, c);
        dfs(r-1, c);
        dfs(r, c+1);
        dfs(r, c-1);
    }

    for(let r =0; r<rows; r++) {
        for(let c=0; c<cols; c++) {
            if(grid[r][c] === '1') {
                dfs(r,c);
                count++;
            }
        }
    }
    return count;
}