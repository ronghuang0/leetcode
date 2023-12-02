// top down
var coinChange = function(coins, amount) {
    let dp = {};
    // coins.sort((a,b)=>a-b);
    // console.log('coins', coins);
    let dfs = (sum) => {
        if(dp[sum] !== undefined) {
            return dp[sum];
        }
        if(sum > amount) {
            return -1;
        }
        if(sum === amount) {
            return 0;
        }
        dp[sum] = Infinity;
        for(let i=coins.length-1; i>=0;i--) {
            let temp = dfs(sum+coins[i]);
            if(temp !== -1) {
                dp[sum] = Math.min(dp[sum], temp+1);
            }  
        }
        return dp[sum] === Infinity ? -1 : dp[sum];
    }
    return dfs(0);
};

// bottom up

var coinChange = function(coins, amount) {
    let dp = {};
    dp[amount] = 0;
    for(let i=amount-1; i>=0; i--) {
        let min = Infinity;
        for(let j=0; j<coins.length;j++) {
            let pastIndex = coins[j] + i;
            if(pastIndex <= amount && dp[pastIndex] !== -1){
                min = Math.min(dp[pastIndex]+1, min);
            }
        }
        if(min === Infinity) {
            dp[i] = -1;
        } else {
            dp[i] = min;
        }
    }
    return dp[0];
};


// neetcode - same but uses array and default values to save on checks
var coinChange = function(coins, amount) {
    let dp = new Array(amount).fill(amount+1);
    dp[amount] = 0;
    for(let i=amount-1; i>=0; i--) {
        for(let j=0; j<coins.length;j++) {
            let pastIndex = coins[j] + i;
            if(pastIndex <= amount && dp[pastIndex] !== -1){
                dp[i] = Math.min(dp[pastIndex]+1, dp[i]);
            }
        }
    }
    return dp[0] === amount +1? -1:dp[0];
};

