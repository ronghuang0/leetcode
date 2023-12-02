// O(n)

var maxProduct = function(nums) {
    let currMax = nums[0];
    let currMin = nums[0];
    let max = nums[0];
    for(let i=1; i<nums.length; i++) {
        temp = Math.max(nums[i], currMax*nums[i], currMin*nums[i]);
        currMin = Math.min(nums[i], currMax*nums[i], currMin*nums[i]);
        currMax = temp;
        max = Math.max(currMax, max );
    }
    return max;
};