// dp, can use map or just use 2 variables
// there is a cleaner way to write this where we calculate the result in two parts instead of the if branches

var numDecodings = function(s) {
    if(s[0] === '0') {
        return 0;
    }
    // store number of ways for that .slice(index)
    // let dp = {};
    // dp[-1] = 1;
    // dp[0] = 1;
    let one = 1;
    let two = 1;
    // if you can have two options: n-1 + n-2
    // if you have one option: n-1
    for(let i = 1; i<s.length; i++) {
        let cat = Number(s[i-1]+s[i]);
        if(s[i] === '0') {
            if(s[i-1] === '1' || s[i-1] === '2') {
                // dp[i] = dp[i-2];
                let temp = two;
                two = one;
                one = temp;
            } else {
                return 0;
            }
        }
        else if(cat <=26 && s[i-1] !== '0'){
            // dp[i] = dp[i-1] + dp[i-2];
            let temp = two;
            two = one + two;
            one = temp;
        } else {
            one = two;
            // dp[i] = dp[i-1];
        }
    }
    return two;
}


//dfs
// there is a cleaner way to write this where we calculate the result in two parts instead of the if branches
var numDecodings = function(s) {
    let dp = {};
    
    let dfs = (i) => {
        if(dp[i]) {
            return dp[i];
        }
        if(s[i] === '0') {
            return 0;
        }
        if(i===s.length-1){
            return 1;
        }
        if(i===s.length) {
            return 1;
        }
       
        let cat = Number(s[i] + s[i+1]);
        if(cat > 26) {
            dp[i] = dfs(i+1);
            return dp[i];
        }
        let left = dfs(i+1);
        let right = dfs(i+2);
        dp[i] = left + right;
        return dp[i];
    }
    return dfs(0);
}