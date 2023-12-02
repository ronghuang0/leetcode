// need to memorize string operations

var isPalindrome = function(s) {
    let start = 0;
    let end = s.length-1;
    while(start<end) {
        if(s[start] !== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
};
// function isPalindrome(str) {
//     return str === str.split('').reverse().join('');
// }
var partition = function(s) {
   let res = [];
   let dfs = function(arr, index, l) {
       if(l === s.length){
           res.push(arr.slice());
           return;
       }
       for(let i = 0; i+index+1<=s.length;i++) {
           let sub = s.substring(index, index+1+i);
           if(!isPalindrome(sub)) {
               continue;
           }
           arr.push(sub);
           dfs(arr, index+i+1, l+i+1);  //i+1 === sub.length
           arr.pop();
       }
   }
   dfs([], 0, 0);
   return res;
};