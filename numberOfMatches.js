var numberOfMatches = function(n) {
    if(n===1){
        return 0;
    }
    if(n%2===1){
        return (n-1)/2 + numberOfMatches(1+(n-1)/2);
    }
    return n/2 + numberOfMatches(n/2);
};