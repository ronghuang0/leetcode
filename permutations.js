

var permute = function(nums) {
    let used = new Array(nums.length).fill(0);
    let res = [];

    function backtrack(curr) {
        if(curr.length === nums.length){
            res.push(curr.slice());
            return;
        }
        for(let i=0; i<nums.length;i++) {
            if(!used[i]) {
                curr.push(nums[i]);
                used[i] = 1;
                backtrack(curr)   
                curr.pop();
                used[i] = 0;
            }
        }
    }
    backtrack([]);
    return res;
};

var permute = function(nums) {
    const res = [];
    const dfs = (index, nums) => {
        if(index === nums.length) {
            res.push(nums.slice());
        }
        for(let i=index; i<nums.length; i++) {
            let temp = nums[i];
            nums[i] = nums[index];
            nums[index] = temp;
            dfs(index+1, nums);
            temp = nums[i];
            nums[i] = nums[index];
            nums[index] = temp;
        }
    }
    dfs(0, nums);
    return res;
};



// class Solution:
//     def permute(self, nums: List[int]) -> List[List[int]]:
        

//         res = []
//         def backtrack(curr, remain):
//             if remain == []:
//                 res.append(curr.copy())
//                 return
            
//             for i in range(len(remain)):
//                 curr.append(remain[i])
//                 backtrack(curr, remain[:i] + remain[i+1:])
//                 curr.pop()
//         backtrack([], nums)

//         return res


// neetcode solution
// nums is popped one by one and the popped letter is saved each level
// after returning from the recursion that is when each element in permutes is appended n back.
// notice that we shift and then we push during the backtracking... this changes the order of nums so when nums is back
// to original length we do it again except w/ new order. Notice how the outer foor loop we don't use the i at all.
var permute = (nums) => {
    let res =[];
    if(nums.length === 1) {
        return [nums.slice()];
    }
    for(let i=0; i<nums.length; i++) {
        let n = nums.shift();
        let permutes = permute(nums);
        for(perm of permutes) {
            perm.push(n);
        }
        nums.push(n);
        res = res.concat(permutes.slice());
    }
    return res;
}
