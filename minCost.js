// Weekly Contest 316 q3
// 2448. Minimum Cost to Make Array Equal

// weighted median
var minCost = function(nums, cost) {
    let tuples = []
    for(let i=0;i<nums.length;i++){
        tuples.push([nums[i], cost[i]]);
    }
    tuples.sort((a,b)=>a[0]-b[0]);
    let total = cost.reduce((curr, accum)=>curr+accum);
    let sum = 0;
    let index = 0;
    while(true){
        sum+=tuples[index][1];
        if(sum>Math.floor(total/2)){
            break;
        }
        index++
    }
    let res =0;
    for(let i=0;i<nums.length;i++){
        res+=Math.abs((nums[i]-tuples[index][0])*cost[i]);
    }
    return res;
};

// binary search
var minCost = function(nums, cost) {
    let findCost = (num) =>{
        let c = 0;
        for(let i=0;i<nums.length;i++){
            c+= Math.abs(nums[i]-num)*cost[i];
        }
        return c;
    }

    let bisectLeft = (l, r) => {
        while(l<r) {
            let mid = Math.floor((l+r)/2);
            let costOne = findCost(mid);
            let costTwo = findCost(mid+1);
            if(costOne > costTwo){
                l = mid+1;
            } else {
                r = mid;
            }
        }
        return l;
    }
    let min = Math.min(...nums);
    let max = Math.max(...nums);
    let res = bisectLeft(min, max);
    return findCost(res)
};