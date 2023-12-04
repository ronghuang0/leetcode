var largestGoodInteger = function(num) {
    let digit = -1;
    for(let i=0;i<num.length-2;i++){
        if(num[i]===num[i+1] && num[i+2]===num[i+1]) { 
            digit = Math.max(digit, Number(num[i]));
        }
    }
    if(digit === -1){
        return '';
    }
    return String(digit).repeat(3);
};