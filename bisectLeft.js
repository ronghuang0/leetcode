
// last occurence

let lastOccurence = (nums, target) =>{
    let l = 0;
    let r = nums.length-1;
    while(l<r){
        let mid = Math.ceil((l+r)/2);
        if(nums[mid] > target){
            r = mid-1;
        } else {
            l = mid;
        }
    }
    return l;
}


// first and last occurence

var searchRange = function(nums, target) {
    let res = [-1, -1];
    let l = 0;
    let r = nums.length-1;
    while(l<=r) {
        let mid = Math.floor((l+r)/2);

        if(nums[mid] === target) {
            res[0] = mid;
        }
        if(nums[mid]>=target) {
            r = mid-1;
        } else {
            l = mid+1;
        }
    }
    l =0;
    r = nums.length-1;
    while(l<=r) {
        let mid = Math.floor((l+r)/2);

        if(nums[mid] === target) {
            res[1] = mid;
        }
        if(nums[mid]>target) {
            r = mid-1;
        } else {
            l = mid+1;
        }
    }
    return res;
};



// bisect left - i like this method because it's easier to think about the edge cases.
// we know that l and r are equal at the end
// we know that we have to do l=mid+1 because our initial mid is left biased, so this way we dont get stuck with same mid
// when target is less than all it's fine since right goes to mid so it won't be negative
// we know the only other edge case is if target is greater than all, so we just return the length
// compare this to using mid+1, mid-1 with (neetcode way), we don't have to think about as many edge cases since in the end l=r

function bisectLeft(nums, n){
    if(nums.length === 0){
        return 0;
    }
    if(n > nums[nums.length-1]) {
        return nums.length;
    }
    let l = 0;
    let r = nums.length-1;
    while(l<r) {
        let mid = Math.floor((l+r)/2);
        if(nums[mid] < n) {
            l = mid+1;
        } else {
            r = mid;
        }
    }
    return l;
}

// if we are doing first/last occurence that is actually different from bisect.
// i like this way of swtching our mid bias based off what we want

var searchRange = function(nums, target) {
  
    let res = [-1, -1];
    if(nums.length === 0) {
        return res;
    }
    let l= 0;
    let r = nums.length-1;
    while(l<r) {
        let mid = Math.floor((l+r)/2);
        if(nums[mid] >= target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    // 5 7 9,  t = 6
    res[0] = nums[l] === target? l:-1;

    l= 0;
    r = nums.length-1;
    while(l<r) {
        let mid = Math.ceil((l+r)/2);
        if(nums[mid] > target) {
            r = mid-1;
        } else {
            l = mid;
        }
    }
    res[1] = nums[l] === target? l:-1;

    // if(res[0] === res[1]) {
    //     return [-1,-1]
    // }
    return res;
};


// biset left, using r = num.length to handle case of target being greater than all
// once r is updated once it becomes left biased
const bisectLeft2 = () =>{
    let l= 0;
    let r = nums.length;
    while(l<r) {
        let mid = Math.floor((l+r)/2);
        if(nums[mid] >= target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l
}

const bisectRight = ()=>{
    let l =0;
    let r = nums.length-1
    while(l<r){
        mid = Math.ceil((l+r)/2)
        if(nums[mid]<= target){
            l = mid;
        } else {
            r = mid-1;
        }
        return l+1
    }
}
