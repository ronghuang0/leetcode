// Weekly Contest 376 q3
// 2967. Minimum Cost to Make Array Equalindromic
var isPalindrome = function(s) {
    let start = 0;
    let end = s.length-1;
    while(start<end) {
        if(s[start]!== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
};

var minimumCost = function(nums) {
    let calc = (val) =>{
        let res =0;
        for(let i=0;i<nums.length;i++){
            res+=Math.abs(nums[i]-val);
        }
        return res;
    }
    nums.sort((a,b)=>a-b);
    let median = Math.floor(nums.length/2);
    let left = nums[median];
    let right = nums[median];
    while(!isPalindrome(String(left))){
        left--;
    }
    while(!isPalindrome(String(right))){
        right++;
    }
    return Math.min(calc(left), calc(right));
};