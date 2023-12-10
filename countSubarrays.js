var countSubarrays = function(nums, k) {
    let count = 0;
    let res = 0;
    let l = 0;
    let max = Math.max(...nums);
    for(let r=0; r<nums.length;r++){
        if(nums[r]===max){
            count++;
        }
        while(count>=k){
            res += nums.length-r;
            if(nums[l]===max){
                count--;
            }
            l++
        }
    }   
    return res;
};