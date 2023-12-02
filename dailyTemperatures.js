// for each element we push into the stack and remove from the stack so it's 2n
// note we only need to store the index in the stack
// monotonic stack

var dailyTemperatures = function(temperatures) {
    const result = new Array(temperatures.length).fill(0);
    const stack = [];
    for(let i=0; i<temperatures.length; i++) {
        while(stack.length && temperatures[stack[stack.length-1]] < temperatures[i]) {
            const index = stack.pop();
            result[index] = i - index;
        }
        stack.push(i);
    }
    return result;
};