// 2482. Difference Between Ones and Zeros in Row and Column
var onesMinusZeros = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let diff = Array.from(Array(m), ()=>Array(n));
    let rowArr = Array(m).fill(0);
    let colArr = Array(n).fill(0);
    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(grid[i][j] === 1){
                rowArr[i]++;
                colArr[j]++;
            }
        }
    }
    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            diff[i][j] = 2*rowArr[i] + 2*colArr[j] - m - n;
        }
    }
    return diff;
};