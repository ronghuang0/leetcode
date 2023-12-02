
// i get tle using an array... this passes w/o the cacheing array though
var findTargetSumWays = function(nums, target) {
    let dp = [];
    let dfs = (index, sum) => {
        
        if(index === nums.length) {
            if(sum === target) {
                return 1;
            }
            return 0;
        }
        if(dp[index] !== undefined && dp[index][sum] !== undefined){
            return dp[index][sum];
        }
        let res = dfs(index +1, sum - nums[index]) + dfs(index+1, sum + nums[index]);
        dp[index]=[];
        dp[index][sum] = res;
        return res;
    }
    return dfs(0, 0);
};

// with map is faster
var findTargetSumWays = function(nums, target) {
    let map = {};
    let dfs = (index, sum) => {
        
        if(index === nums.length) {
            if(sum === target) {
                return 1;
            }
            return 0;
        }
        if(map[`${index}_${sum}`] !== undefined){
            return map[`${index}_${sum}`];
        }
        let res = dfs(index +1, sum - nums[index]) + dfs(index+1, sum + nums[index]);
        map[`${index}_${sum}`] = res;
        return res;
    }
    return dfs(0, 0);
};