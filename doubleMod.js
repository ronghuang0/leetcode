// Weekly Contest 375 q2
// 2961. Double Modular Exponentiation
var power = function(a, b, n) {
    if(b===0){
        return 1;
    }
    if(b%2!==0){
        return ((a%n)*(power(a, b-1, n)%n))%n;
    }
    return (power(a,b/2,n)%n*power(a,b/2,n)%n)%n;
};
var getGoodIndices = function(variables, target) {
    let res = [];
    for(let i=0;i<variables.length;i++){
        let [a, b, c, m] = variables[i];
        let f = power(a, b, 10);
        let calc = power(f, c, m);
        if(calc === target){
            res.push(i);
        }
    }
    return res;
};