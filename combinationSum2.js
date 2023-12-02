var combinationSum2 = function(candidates, target) {
	candidates.sort((a,b)=>a-b);
    let res = [];
    let popped;
    let dfs = (nums, sum, i) => {
        if(sum === target) {
            res.push(nums.slice());
            return;
        }
        if(sum > target) {
            return;
        }
        for(let j =i; j<candidates.length; j++) {
            if(candidates[j] === popped) {
                continue;
            }
            nums.push(candidates[j]);
            dfs(nums, sum+candidates[j], j+1);
            popped = nums.pop();
        }
    }
    dfs([], 0, 0);
    return res;
}

// binary solution - funny note: in neetcodes video he draws up a binary decision tree but then codes up the for loop tree

var combinationSum2 = function(candidates, target) {
    candidates.sort((a,b)=>a-b);
    let res = [];
    let popped;
    let dfs = (nums, sum, i) => {
        if(sum === target) {
            res.push(nums.slice());
            return;
        }

        if(sum>target || i === candidates.length) {
            return;
        }
        
        nums.push(candidates[i])
        dfs(nums, sum+candidates[i], i+1);
        popped = nums.pop();
        while(popped === candidates[i+1] && i+1!==candidates.length) {
            i++
        }
        dfs(nums, sum, i+1);
        
    }
    dfs([], 0, 0);
    return res;
}