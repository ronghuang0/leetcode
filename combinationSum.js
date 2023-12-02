
// useful tip - a common tool is to do for (let i = index; ... ) we have to map what these things do to the decision tree
// for loop - this populates one level of tree
// dfs() - each call goes 1 level deeper in the tree
// function dfs(index, curr)
// call of dfs(index + 1) this means as we go deeper the starting i is incremented, but as we go to the right (for loop, same level) the index stays the same
// call of dfs(i) this means as we go deeper the starting i is the same, but as we go to the right (for loop, same level) the i is used as the starting index 
// so the starting i is incremented
var combinationSum = function(candidates, target) {
    let res = [];
    let dfs = (curr, sum, index) => {
        if(sum === target) {
            res.push(curr.slice());
            return;
        } else if(sum > target) {
            return;
        }

        for(let i=index; i<candidates.length; i++) {
            curr.push(candidates[i]);
            dfs(curr, sum + candidates[i], i);
            curr.pop();
        }
    }
    dfs([], 0, 0);
    return res;
};






// neetcode likes to use the binary decision tree, this usually involves two dfs() and no for loop
// the logic for this is - left we add the number, right we don't. and as we keep going we do it with
// the next numbers in the array (i have no idea how to explain it - seems like drawing is the best way)

// notice we check the index... what happens if we dont check the index? the index will be out of bounds, undefined, and infinite loop

var combinationSum = (candidates, target) => {
    let res = []

    let dfs=(nums, sum, index)=>{
        if(sum === target) {
            res.push(nums.slice());
            return;
        }
        if(sum > target || index === candidates.length) {
            return;
        }
     
        nums.push(candidates[index]);
        dfs(nums, sum+candidates[index], index);
        nums.pop();
        dfs(nums, sum, index+1);
    }
    dfs([], 0, 0);

    return res;
}

let dog = [2];
console.log('hi', combinationSum(dog, 1));