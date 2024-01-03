// max heap solution



// min heap solution






// n + n/2 + n/4 + n/8 + ... + 1 = x
// 2n + n + n/2 + n/4 + ... + 2 = 2x
// 2n + 2 = x

//O(n)



// when i did this problem again i did it iteratively. it got TLE and it took me a long time to realize that i forgot to update the left and right boundaries
// in my iterative version.

var findKthLargest2 = function(nums, k) {
    let count = 0;
    function swap(a, b) {
        let temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
    
    function partition(l, r) {
        count++;
        let pivot = nums[r];
        let i =l;
        for(let j=l; j<r;j++) {
            if(nums[j]>pivot){
                swap(i, j);
                i++;
            }
        }
        swap(i, r);
        return i;
    }
    let l = 0;
    let r = nums.length-1;
    let i = partition(l, r);
    while(true) {
        if(i === k-1) {
            return nums[i];
        } else if(k-1>i) {
            l = i+1;
            i = partition(l, r);
        } else {
            r = i-1;
            i = partition(l, r);
        }
    }
};




var findKthLargest = function(nums, k) {
    const swap = (a, b) => {
        let temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
    const partition = (l, r) => {
        let pivot = nums[r];
        let i = l;
        for(let j=l; j<r;j++){
            if(nums[j]>pivot) {
                swap(i, j);
                i++;
            } 
        }
        swap(i, r);
        return i;
    }
    
    const search = (l, r) => {
        
        let i = partition(l, r);

        if(i === k-1) {
            
            return nums[i];
        } else if(k-1>i) {
            
            return search(i+1, r);
        } else {
            
            return search(l, i-1);
        }
    }
    let l = 0;
    let r = nums.length-1;
    let res = search(l,r);
    return res;
    
};
