/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function(n, ranges) {
    let arr = [];
    for(let i=0;i<ranges.length;i++) {
        if(ranges[i] === 0) {
            continue;
        }
        let left = i-ranges[i] < 0? 0:i-ranges[i];
        let right = i+ranges[i];
        arr.push([left, right]);
    }
    arr.sort((a,b)=>a[0]-b[0]);
    let prevR = 0;
    let currR = 0;
    let res = 1;
    for(let i=0;i<arr.length;i++){
        let [l,r] = arr[i];
        if(l>currR){
            return -1;
        }
        if(l<=prevR && r>currR) {
            // prevR = prevR; stays same
            currR = r;
        }else if(l>prevR && r> currR) {
            res++;
            prevR=currR;
            currR=r;
        }
        if(currR>=n) {
            return res;;
        }
    }
    return -1;
};




// O(n)
// leetcode is missing 1 test case :joy

var minTaps = function(n, ranges) {
    let arr = [];
    for(let i=0;i<ranges.length;i++) {
        if(ranges[i] === 0) {
            continue;
        }
        let left = i-ranges[i] < 0? 0:i-ranges[i];
        let right = i+ranges[i];
        arr[left] = Math.max(arr[left] || 0, right);
    }
    let prevR = 0;
    let currR = 0;
    let res = 1;
    for(let i=0;i<arr.length;i++){
        let l = i;
        let r = arr[i];
        if(l>currR){
            return -1;
        }
        if(l<=prevR && r>currR) {
            // prevR = prevR; stays same
            currR = r;
        }else if(l>prevR && r> currR) {
            res++;
            prevR=currR;
            currR=r;
        }
        if(currR>=n) {
            return res;;
        }
    }
    return -1;
};