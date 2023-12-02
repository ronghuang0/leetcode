
var climbStairs = function(n) {
    let map = {};
    let traverse = (n)=>{
        if(n === 1) {
            return 1;
        }
        if(n===2) {
            return 2;
        }
        if(map[n] !== undefined) {
            return map[n];
        }
        let one = traverse(n-1);
        map[n-1] = one;
        let two = traverse(n-2);
        return one+two;
    }
    return traverse(n);
};


// dp

var climbStairs = function(n) {
    if(n===1) return 1;
    if(n===2) return 2;
    let one = 1;
    let two = 2;
    for(let i=3; i<=n; i++) {
        let temp = two;
        two = one + two;
        one = temp;
    }
    return two;
};