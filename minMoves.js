// 462. Minimum Moves to Equal Array Elements II
// find median
var minMoves2 = function(nums) {
    nums.sort((a,b)=>a-b);
    let n = nums[Math.floor(nums.length/2)];
    let res = 0;
    for(let i=0;i<nums.length;i++){
        res+= Math.abs(nums[i]-n);
    }
    return res;
};

// use difference between elements
var minMoves2 = function(nums) {
    nums.sort((a,b)=>a-b);
    let n = nums.length/2;
    let res = 0;
    for(let i=0;i<n;i++){
        res+= nums[nums.length-1-i] - nums[i];
    }
    return res;
};