// 2353. Design a Food Rating System

// binary search
let compare = (a, b) => {
    let res = a[0]-b[0];
    if(res===0){
        return b[1].localeCompare(a[1]);
    }
    return res;
}

 let bisectLeft = (nums, target) => {
    let l= 0;
    let r = nums.length;
    while(l<r) {
        let mid = Math.floor((l+r)/2);
        let c = compare(nums[mid], target);
        if(c>=0) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l
 }

var FoodRatings = function(foods, cuisines, ratings) {
    this.foodsId = {};
    this.tuples = [];
    this.cuisines = cuisines;
    for(let i=0;i<foods.length;i++){
        this.foodsId[foods[i]] = i;
        this.tuples[i] = [ratings[i], foods[i]];
    }
    
    this.map = {};
    for(let i=0;i<foods.length;i++){
        if(this.map[cuisines[i]]===undefined) {
            this.map[cuisines[i]] = [];
        }
        this.map[cuisines[i]].push(this.tuples[i]);
    }
    for(let k in this.map){
        this.map[k].sort(compare); // highest rated last
    }
};

FoodRatings.prototype.changeRating = function(food, newRating) {
    let id = this.foodsId[food];
    let arr = this.map[this.cuisines[id]];
    let removeIndex = bisectLeft(arr, this.tuples[id]);
    arr.splice(removeIndex, 1); 
    this.tuples[id][0] = newRating;
    this.tuples[id][1] = food;
    let addIndex = bisectLeft(arr, this.tuples[id]);
    arr.splice(addIndex, 0, this.tuples[id]);
};

FoodRatings.prototype.highestRated = function(cuisine) {
    return this.map[cuisine][this.map[cuisine].length-1][1];
};


// heap
let compare2 = (a, b) => {
    let res = b[0]-a[0];
    if(res===0){
        return a[1].localeCompare(b[1]);
    }
    return res;
}

var FoodRatings = function(foods, cuisines, ratings) {
    this.foodsId = {};
    this.cuisines = cuisines;
    this.ratings = ratings;
    for(let i=0;i<foods.length;i++){
        this.foodsId[foods[i]] = i;
    }
    
    this.map = {};
    for(let i=0;i<foods.length;i++){
        if(this.map[cuisines[i]]===undefined) {
            this.map[cuisines[i]] = new PriorityQueue({compare});
        }
        this.map[cuisines[i]].enqueue([ratings[i], foods[i]]);
    }
};

/** 
 * @param {string} food 
 * @param {number} newRating
 * @return {void}
 */
FoodRatings.prototype.changeRating = function(food, newRating) {
    let id = this.foodsId[food];
    this.ratings[id] = newRating;
    let heap = this.map[this.cuisines[id]];
    heap.enqueue([newRating, food]);  
};

/** 
 * @param {string} cuisine
 * @return {string}
 */
FoodRatings.prototype.highestRated = function(cuisine) {
    let f = this.map[cuisine].front();
    while(this.ratings[this.foodsId[f[1]]] !== f[0]) {
        this.map[cuisine].dequeue();
        f = this.map[cuisine].front();
    }
    return f[1];
};
