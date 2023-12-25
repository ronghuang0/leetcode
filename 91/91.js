// 91. Decode Ways

// dfs

let decodeWays = (s)=> {
    let dp = {};

    let dfs = (i) => {
        // if we don't specify undefined it's as if we didn't memoize the zero results
        if(dp[i] !== undefined) {
            return dp[i];
        }
        if(s[i] = 0) {
            return 0;
        }
        if(i >= s.length) {
            return 1;
        }
        let res = s[i+1];
        let cat = Number(s[i]+s[i+1]);
        if(cat <= 26) {
            res += s[i+2];
        }
        dp[i] = res;
        return res;
    }
    return dfs(0);
}


// bottom up  from left to right

let numDecodings2 = (s) => {
    if(s[0] === '0') {
        return 0;
    }
    let dp = {};
    dp[-1] = 1;
    dp[0] = 1;
    for(let i=1; i<s.length; i++) {
        if(s[i]==='0') {
            if(s[i-1] === '1' || s[i-1] === '2') {
                dp[i] = dp[i-2];
                continue;
            } else {
                return 0;
            }
        }
        let cat = Number(s[i-1]+s[i]);
        if(cat <= 26 && s[i-1] !== '0') {
            dp[i] = dp[i-1] + dp[i-2]; 
        } else {
            dp[i] = dp[i-1];
        }
    }
    return dp[s.length-1];
}

// bottom up from right to left, my messy version
// how do we make the clean version the first time???? it seems like sometimes the clean version isn't the most intuitive

let numDecodings3 = (s) => {
    let dp = {};
    dp[s.length] = 1;
    for(let i=s.length-1; i>=0; i--) {
        if(s[i]==='0') {
            dp[i] = 0;
            continue;
        }
        let cat = Number(s[i] + s[i+1]);
        if(cat <= 26 && s[i+1] !== '0' && s[i+2] !== '0') {
            dp[i] = dp[i+1] + dp[i+2];
        } else {
            if(s[i+1] === '0') {
                if(cat <= 26) {
                    dp[i] = dp[i+2];
                } else {
                    dp[i] = 0;
                }
            } else {
                 dp[i] = dp[i+1];
            }
        }
    }
    return dp[0];
}

// better version
let numDecodings = (s) => {
    let dp = {};
    dp[s.length] = 1;
    for(let i=s.length -1; i>=0;i--) {
        if(s[i] === '0') {
            dp[i] = 0;
            continue;
        }
        dp[i] = dp[i+1];
        let cat = Number(s[i] + s[i+1]);
        if(cat <= 26) {
            dp[i] += dp[i+2];
        }
        
    }
    return dp[0];
}