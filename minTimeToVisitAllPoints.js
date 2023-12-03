var minTimeToVisitAllPoints = function(points) {
    let res = 0;
    for(let i=1;i<points.length;i++){
        let [x, y] = points[i-1];
        let [a, b] = points[i];
        res += Math.max(Math.abs(a-x), Math.abs(b-y));
    }
    return res;
};