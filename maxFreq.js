// 1838. Frequency of the Most Frequent Element

// Sliding Window
var maxFrequency = function(nums, k) {
    nums.sort((a,b)=>a-b);
    let l = 0;
    let curr = 0;
    let res = 0;
    for(let r=0;r<nums.length;r++){
        curr += nums[r];
        while((nums[r]*(r-l+1)-curr)>k){
            curr-=nums[l];
            l++;
        }
        res = Math.max(res, r-l+1);
    }
    return res;
};