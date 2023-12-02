//dfs

var wordBreak = function(s, wordDict) {

    let dp = {};
    let dfs = (index) => {
      if(index === s.length) {
        return true;
      }
      for(let i=0; i<wordDict.length;i++) {
        let n = wordDict[i].length;
        if(s.slice(index, index+n) === wordDict[i]){
          if(dp[index+n] === false) {
            continue
          }
          if(dfs(index+n)) {
            return true;
          }
          dp[index+n] = false;
        }
      }
      return false;
    }
    return dfs(0);
    
  };

  // dp

  var wordBreak = function(s, wordDict) {
    let dp = new Array(s.length+1).fill(false);
    dp[s.length] = true;
    for(let i = s.length-1; i>=0; i--) {
      for(let j=0; j<wordDict.length; j++) {
        let w = wordDict[j];
        if(w.length <= s.length-i && s.slice(i, i+w.length) === w){
          dp[i] = dp[i+w.length];
          if(dp[i] === true) {
            break;
          }
        }
      }
    }
    return dp[0];
  };