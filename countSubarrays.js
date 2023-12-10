// Weekly Contest 375 q3
// 2962. Count Subarrays Where Max Element Appears at Least K Times

// sliding window
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

// hash table
var countSubarrays2 = function(nums, k) {
    let arr = [];
    let map = {};
    let max = Math.max(...nums);
    let count = 0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]===max){
            count++;
        }
        arr[i] = count;
        if(map[count] === undefined){
            map[count] = i;
        }
    }
    let res = 0;
    for(let i=0;i<nums.length;i++){
        let target;
        if(nums[i] === max){
            target = arr[i]+k-1;
        } else{
            target = arr[i]+k;
        }
        if(map[target] !== undefined){
            res+=nums.length-map[target];
        }
    }
    return res;
};

// prefix sum + binary search
let search = (l, r, arr, target)=>{
    while(l<r){
        let mid = Math.floor((l+r)/2);
        if(arr[mid]<target){
            l = mid+1;
        } else {
            r = mid;
        }
    }
    return l;
}
var countSubarrays3 = function(nums, k) {
    let max = Math.max(...nums);
    let counts = [];
    let count = 0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]===max){
            count++;
        }
        counts[i]=count;
    }
    let res = 0;
    for(let i=0;i<nums.length;i++){
        if(counts[i] >= k){
            let start = search(0, i, counts, counts[i]-k+1);
            res+=start+1;
        }
    }
    return res;
};