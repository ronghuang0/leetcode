//top down - we actually only need 2 arguments since s3 is always s1+s2

var isInterleave = function(s1, s2, s3) {
    let dp = {};
    if(s1.length + s2.length !== s3.length ) {
        return false;
    }
    let dfs = (a, b, c) => {
        if(dp[`${a}_${b}_${c}`] !== undefined) {
            return dp[`${a}_${b}_${c}`];
        }
        if(c === s3.length) {
            return true;
        }
        if(s1[a] === s3[c] && s2[b] === s3[c]) {
            dp[`${a}_${b}_${c}`] = dfs(a+1, b, c+1) || dfs(a, b+1, c+1);
        } else if(s1[a] === s3[c]) {
            dp[`${a}_${b}_${c}`] = dfs(a+1, b, c+1);
        } else if(s2[b] === s3[c]){
            dp[`${a}_${b}_${c}`] = dfs(a, b+1, c+1);
        } else {
            dp[`${a}_${b}_${c}`] = false;
        }
        return dp[`${a}_${b}_${c}`];
    }
    return dfs(0, 0, 0);
};


//bottom up

var isInterleave = function(s1, s2, s3) {
    if(s1.length + s2.length !== s3.length) {
        return false;
    }
    let dp = {};
    dp[`${s1.length}_${s2.length}`] = true;
    for(let a = s1.length; a>=0; a--) {
        for(let b=s2.length; b>=0;b--) {
            if(a === s1.length && b === s2.length){
                continue;
            }
            dp[`${a}_${b}`] = false;
            if(s3[a+b] === s1[a] && dp[`${a+1}_${b}`]) {
                dp[`${a}_${b}`] = true;
            }
            if(s3[a+b] === s2[b] && dp[`${a}_${b+1}`]) {
                dp[`${a}_${b}`] = true;
            }
        }
    }
    return dp['0_0'];
};

// using O(n) space
var isInterleave = function(s1, s2, s3) {
    if(s1.length + s2.length !== s3.length) {
        return false;
    }
    let row = [];
    for(let i = s1.length; i>=0; i--) {
        for(let j=s2.length; j>=0;j--) {
            if(i === s1.length && j === s2.length){
                row[j] = true;
                continue;
            }
            row[j] = (s3[i+j] === s1[i] && row[j]) || (s3[i+j] === s2[j] && row[j+1])
        }
    }
    return row[0];
};