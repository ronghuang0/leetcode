var minCostClimbingStairs = function(cost) {
    let n = cost.length;
    let zero = 0;
    let one = 0;
    for(let i = 2; i<=n; i++) {
        let temp = one;
        one = Math.min((zero+cost[i-2]), (one+cost[i-1]));
        zero = temp;
    }
    return one;
};