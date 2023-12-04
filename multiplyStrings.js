var multiply = function(num1, num2) {
    num1 = num1.split('').reverse().join('');
    num2 = num2.split('').reverse().join('');
    if(num2.length>num1.length){
        let temp = num1;
        num1 = num2
        num2 = temp
    }
    let res = Array(num1.length+num2.length).fill(0);
    for(let i=0;i<num2.length;i++){
        for(let j=0;j<num1.length;j++){
            let product = Number(num2[i])*Number(num1[j]);
            res[i+j] += product;
            res[i+j+1] += Math.floor(res[i+j]/10);
            res[i+j] = res[i+j]%10;
        }
    }
    let end = res.length-1;
    while(end > 0 && res[end] === 0){
        end--;
    }
    return res.slice(0,end+1).reverse().join('');
};