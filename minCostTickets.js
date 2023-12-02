// bottom up
var mincostTickets = function(days, costs) {
    // index of the day closest to being out of 7 range
    let seven=0;
    //index of the day closest to being out of 30 range
    let thirty=0;
    //min cost of travelling every day including that day
    let arr = [];
    arr[-1]=0;
    // i represents travelling up to and including i
    for(let i=0; i<days.length; i++) {
        while(days[i] - days[seven] >= 7) {
            seven = seven+1;
        }
        while(days[i]-days[thirty] >= 30) {
            thirty = thirty+1;
        }
        arr[i] = Math.min(arr[i-1] + costs[0], arr[seven-1]+costs[1], arr[thirty-1] + costs[2]);
    }
    return arr[days.length-1];
};


// top down
// neetcode's solution for this goes from i=0 to 50 ...
var mincostTickets = function(days, costs) {
    let dp = {};
    days[-1] = 0;
    let dfs = (i)=>{
        // need to think about base cases more, doesn't hurt to add extra lol. at first i only had i===0
        // if(i === 0) {
        //     return costs[0];
        // }
        if(i===-1) {
            return 0;
        }
        if(dp[i] !== undefined) {
            return dp[i];
        }
        let weekIndex = i;
        let monthIndex = i;
        while(days[i]-days[weekIndex] < 7 && weekIndex > -1) {
            weekIndex--;
        }
        // when i copy pasted the while loop i didn't change weekindex to month index and it took me a while to find
        // ppl seem to like to use a loop and not write this code again
        while(days[i]-days[monthIndex] < 30 && monthIndex > -1) {
            monthIndex--;
        }
        dp[i] = Math.min(dfs(i-1)+costs[0], dfs(weekIndex)+costs[1], dfs(monthIndex)+costs[2]);
        
        return dp[i];
    }
    return dfs(days.length-1);

};