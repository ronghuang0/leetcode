// 2676. Throttle

var throttle = function(fn, t) {
    let nextArgs = null;
    let curr = false;
    let call = () => {
        if(nextArgs === null){
            curr = false
        } else {
            fn(...nextArgs)
            nextArgs = null;
            setTimeout(call, t)
        }
    }
    return function(...args) {
        if(!curr){
            fn(...args)
            curr = true;
            setTimeout(call, t)
        } else {
            nextArgs = args
        }
    }
};