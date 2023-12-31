// dp with 2d array
var lengthOfLIS = function(nums) {
    nums[-1] = -100001
    let dp = Array.from(Array(nums.length), ()=>Array(nums.length));
    dp[nums.length] = Array(nums.length+1).fill(0);
    for(let i = nums.length-1;i>=0; i--){
        for(let j =nums.length-2;j>=-1;j--) {
            let skip = dp[i+1][j+1];
            let keep = nums[i]>nums[j] ? dp[i+1][i+1]+1:0;
            dp[i][j+1] = Math.max(skip, keep);
        }
    }
    return dp[0][0];
};

//dp with less memory
var lengthOfLIS = function(nums) {
    nums[-1] = -100001
    let next = Array(nums.length+1).fill(0);
    for(let i = nums.length-1;i>=0; i--){
        for(let j =nums.length-2;j>=-1;j--) {
            let skip = next[j+1];
            let keep = nums[i]>nums[j] ? next[i+1]+1:0;
            next[j+1] = Math.max(skip, keep);
        }
    }
    return next[0];
};

// dfs - each call is longest w/ that index as the start
var lengthOfLIS = function(nums) {
    let dp = {};
    let res = 1;
    let dfs = (index) => {
        if(dp[`${index}`] !== undefined) {
            return dp[`${index}`];
        }
        let longest = 1;
        for(let i=index+1; i<nums.length;i++) {
            if(nums[i] > nums[index]) {
                longest = Math.max(longest, 1+dfs(i));
            }
        }
        res = Math.max(res, longest);
        dp[`${index}`] = longest;
        return longest;
    }
    nums.forEach((num, i)=>{
        dfs(i);
    })

    return res;
};

// different dfs
var lengthOfLIS = function(nums) {
    l = nums.length
    nums[-1] = -10001;
    let dp = Array.from(Array(l), ()=>Array(l))
    let dfs = (index, prev) => {
        if(index === l) {
            return 0;
        }
        if(dp[index][prev] !== undefined) {
            return dp[index][prev];
        }
        let left = 0;
        if(nums[index] > nums[prev]) {
            left = 1+dfs(index+1, index);
        }
        let right = dfs(index+1, prev);
        dp[index][prev] = Math.max(left, right);
        return dp[index][prev];
    }
    return dfs(0, -1);
};

// patience sort - this only needs length so we dont need to do it but id like to see the pointer implementation to get actual sequence
// get better at implementing bisect left/right
// so many variables - choosing mid towards right vs left, choosing initial l<r vs l<=r, choosing both increment 1 on mid, choosing only one 
// to be increment mid, what to return at the end???

var lengthOfLIS = function(nums) {
    function search(n){
        if(stacks.length === 0){
            return 0;
        }
        let l = 0;
        let r = stacks.length;
        while(l<r) {
            // let mid = Math.floor((l+r)/2);
            let mid = l+ Math.floor((r-l)/2);
            if(n === stacks[mid]){
                return mid;
            } else if(n > stacks[mid]) {
                l = mid+1;
            } else { // n < stacks[mid]
                r = mid;
            }
        }
        if(r === -1){
            return 0;
        }
        return l;
        // return stacks[r] < n ? r+1: r;
    }
    let stacks = []; // each index holds the lowest value at that stack
    for(let i=0; i<nums.length;i++) {
        let index = search(nums[i]);
        stacks[index] = nums[i];
    }
    return stacks.length;
    
};