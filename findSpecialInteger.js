//1287. Element Appearing More Than 25% In Sorted Array

//binary search
let findLast = (arr, target) =>{
    let l=0;
    let r=arr.length-1;
    while(l<r){
        let mid = Math.ceil((l+r)/2);
        if(arr[mid]<=target){
            l=mid;
        } else {
            r=mid-1;
        }
    }
    return l;
}
let findFirst = (arr, target) =>{
    let l=0;
    let r=arr.length-1;
    while(l<r){
        let mid = Math.floor((l+r)/2);
        if(arr[mid]<target){
            l=mid+1;
        } else {
            r=mid;
        }
    }
    return l;
}
var findSpecialInteger = function(arr) {
    let n = arr.length;
    let one = Math.floor(n/4);
    let two = Math.floor(n/2);
    let three = Math.floor(n*3/4);
    let candidates = [arr[one], arr[two], arr[three]];
    for(let i=0;i<candidates.length;i++){
        let first = findFirst(arr, candidates[i]);
        let last = findLast(arr, candidates[i]);
        if((last-first+1)>(n/4)){
            return candidates[i];
        }
    }
};