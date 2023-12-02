// iterative
// time complexity: n*2^n   There are 2^n subsets and the average size of a subset is n/2. Every subset takes n/2 time to copy into the result.
// space complexity: n*2^n from res and n from others  There are 2^n subsets w/e average size of n/2, so result is size n*2^n. 
// the other array is n because at every inner loop we are creating a copy of a set and adding it to res, the size of a set is avg n/2

var subsets = function(nums) {
    const res = [[]];
    for(let i=0;i<nums.length;i++) {
        let resLength = res.length;
        for(let j=0;j<resLength; j++) {
            let copy = res[j].slice();
            copy.push(nums[i]);
            res.push(copy);
        }
    }
    return res;
};


// recursive
// time complexity: n*2^n   same logic as above, the main computations are just copying the subsets into result
// space complexity: n*2^n  for result array.  n for the subset that is created when going from root to last level of tree. the array grows from
// 1 to n, so max is n

// here there are two choices for each element - include or not include. We then go down the decision tree for both of those choices.
// neetcode
var subsets2 = function(nums) {
    let res = [];
    let subset = [];
    const traverse = (i)=>{
        if(i===nums.length){
            res.push(subset.slice());
            return;
        }
        subset.push(nums[i]);
        traverse(i+1);
        subset.pop();
        traverse(i+1)
    }
    traverse(0);
    return res;
};

//recursive w/ for loop

var subsets3 = function(nums) {
    let res = [[]];
    function dfs(curr, index) {
        for(let i=index; i<nums.length; i++) {
            curr.push(nums[i]);
            res.push(curr.slice());
            dfs(curr, i+1);
            curr.pop();
        }
    }
    dfs([], 0);
    return res;
};


