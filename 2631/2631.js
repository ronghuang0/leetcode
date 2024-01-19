// 2631. Group By

Array.prototype.groupBy = function(fn) {
    let res = {}
    for(let i=0;i<this.length;i++){
        let key = fn(this[i]);
        if(res[key] === undefined) {
            res[key] = [];
        }
        res[key].push(this[i])
    }
    return res;
};