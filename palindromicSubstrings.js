// for each index you think how many palindromes is this the middle?
// this works because if you look at all the palindromes in a  string and group them into buckets of mid index, it will all separate into
// differet ones - no repeats. Also, we can think of mid as closer mid so it works for even and odd.

// O(n^2)
var countSubstrings = function(s) {
  let total = 0;

  for(let i=0; i<s.length; i++) {
    //check odd
    let l = i;
    let r = i;
    while(l>=0 && r<s.length && s[l] === s[r]) {
      total++;
      l--;
      r++;
    }
    // check even
    l = i;
    r = i+1;
    while(l>=0 && r<s.length && s[l] === s[r]) {
      total++
      l--;
      r++;
    }
  }
  return total;
}
