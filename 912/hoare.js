
// if we use last element as pivot an infinite loop is possible
// the pivot we choose in the beginning usually isn't going to be in the index that we return
// the index that we do return doesn't necessarily even split up the array based off of the initial pivot ex- [5, 2, 3, 1]
// when we use 5 as pivot for this, the index returned in 2. What it returns is an index so that nothing on the left side (including pivot)
// is greater than the right side.

function partition(arr, low, high)
{
    let pivot = arr[low];
    let i = low - 1, j = high + 1;

    while (true) {
        // Find leftmost element greater
        // than or equal to pivot
        do {
            i++;
        } while (arr[i] < pivot);

        // Find rightmost element smaller
        // than or equal to pivot
        do {
            j--;
        } while (arr[j] > pivot);

        // If two pointers met.
        if (i >= j)
            return j;
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        // swap(arr[i], arr[j]);
    }
}

var sortArray = function(nums) {
    const swap = (a,b)=>{
        let temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
    let l = 0;
    let r = nums.length-1;
    const sort = (l, r) => {
        if(l >= r) return;
        let pi = partition(nums, l, r);
        sort(l, pi);
        sort(pi+1, r);
    }
    sort(l,r);
    return nums;
};


// let dog = [1, 2, 3, 5];
// let dog = [5,2,3,1];
// dog = [5,1,1,2,0,0];
// console.log('j', partition(dog, 0, 3));
// console.log('nums', sortArray(dog));



/* from wiki
With respect to this original description, implementations often make minor but important variations. Notably, the scheme as presented 
below includes elements equal to the pivot among the candidates for an inversion (so "greater than or equal" and "less than or equal" tests 
are used instead of "greater than" and "less than" respectively; since the formulation uses do...while rather than repeat...until which is 
actually reflected by the use of strict comparison operators */
//edge cases: some cases when pivot is greatest or smallest element. when every element is the same.
// another solution: randomizing the pivot will also fix the infinite loops (i think)
// my best guess at what the original version was: 


const swap = (nums, a,b)=>{
    let temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

const partition2 = (nums, l, r) => {
    // let pivot = nums[l];
    let pivotIndex = Math.floor((l+r)/2);
    let pivot = nums[pivotIndex];
    let start = l; 
    let end = r;
    while(l<=r) {
        while(l<=r && nums[l] <= pivot) {
            l++;
        }
        // handling the edge case of the pivot being the greatest element and the left pointer being able to reach the right boundary
        // if it reaches the boundary we know that the pivot is the greatest and that it was never swapped so we can swap the pivot 
        // with the element at the end and tell next sort to not include the pivot (end of array) in the sort by moving the returned 
        // index
        if(l=== end +1) {
            swap(nums, pivotIndex, end);
            return [end-1, end];
        }
        while(l<=r && nums[r] >= pivot) {
            r--;
        }
        // same for other case. I don't think there is a way to do this by returning only 1 index.
        if(r === start-1) {
            swap(nums, pivotIndex, start);
            return [start, start+1];
        }
   
        if(l > r) {
            return [r, r+1];
        }
        swap(nums, l,r);
        l++;
        r--;
    }
    
    return [r, r+1];
}

var sortArray2 = function(nums) {
    let l = 0;
    let r = nums.length-1;
    const sort = (l, r) => {
        if(l >= r) return;
        let [lp, rp] = partition2(nums, l, r);
        sort(l, lp);
        sort(rp, r);
    
    }
    sort(l,r);
    return nums;
};


// let dog = [5,1,1,2,0,0];
// let dog = [1, 2, 3, 5];
// let dog = [5,2,3,1];
// let dog = [-1,2,-8,-10];
// let dog = [-8,2];
// let dog = [-1, -10, -8]
// sortArray2(dog);
// console.log('dog', dog);
// console.log(sortArray2(dog));

//1 2 3 4 5



// another version - this one uses < for the two pointers and also uses a regular while loop. 

var sortArray3 = function(nums) {
    const partition = (l, r) => {
        let pivot = nums[Math.floor((l+r)/2)];
        while(l<=r) {
            while(l<=r && nums[l] < pivot) {
                l++;
            }
            while(l<=r && nums[r] > pivot) {
                r--;
            }
            if(l<=r){
                swap(l,r);
                l++;
                r--;
            }
        }
        return [r, l];
    }
    const swap = (a,b)=>{
        let temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
    let l = 0;
    let r = nums.length-1;
    const sort = (l, r) => {
        if(l >= r) return;
        console.log('l', l);
        console.log('r', r);
        console.log('nums', nums);
        let [lp, rp] = partition(l, r);
        sort(l, lp);
        sort(rp, r);
    }
    sort(l,r);
    return nums;
};

let dog = [5, 2, 3, 1];

sortArray3(dog);