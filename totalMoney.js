var totalMoney = function(n) {
    let weeks = Math.floor(n/7);
    let days = n%7;
    return 28*weeks+3.5*weeks*(weeks-1) + days*(weeks+1)+days*(days-1)/2;
};