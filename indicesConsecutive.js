// google doc interview
// given string return array of tuples of consecutive characters 3 or greater
let func = (string) =>{
    let last = 0;
    let res = [];
    for(let i=1;i<string.length;i++){
        if(string[i] === string[i-1]){
            if(i-last === 2) {
                res.push([last, i]);
            } else if(i-last > 2){
                res[res.length-1][1] = i;
            }
        } else {
            last = i;
        }
    }
    return res;
}

console.log(func('heeeeoollll'));
console.log(func('heeeeoolllloooo'));
console.log(func(''))