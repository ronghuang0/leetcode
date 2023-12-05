var DetectSquares = function() {
    this.counter = {};
};

/** 
 * @param {number[]} point
 * @return {void}
 */
DetectSquares.prototype.add = function(point) {
    let [x,y] = point;
    this.counter[`${x}-${y}`] = (this.counter[`${x}-${y}`] || 0 ) + 1;
};

/** 
 * @param {number[]} point
 * @return {number}
 */
DetectSquares.prototype.count = function(point) {
    let [x,y] = point;
    let res = 0;
    for(let key in this.counter){
        let [nx, ny] = key.split('-');
        nx = Number(nx);
        ny = Number(ny);
        if(Math.abs(x-nx) === Math.abs(y-ny) && x !== nx){
            res+= (this.counter[`${nx}-${ny}`] || 0)*(this.counter[`${x}-${ny}`] || 0)*(this.counter[`${nx}-${y}`] || 0);
        }
    }
    return res;
};