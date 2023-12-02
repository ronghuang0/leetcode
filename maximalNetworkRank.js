// in python it's much less annoying. We don't need to check if graph key has been set and if we do .has or .size on something that hasn't been set it still works

var maximalNetworkRank = function(n, roads) {
    // if(roads.length === 0) return 0;
    let graph = {};
    for(let [i, j] of roads) {
        if(!graph[i]){
            graph[i] = new Set();
        }
        graph[i].add(j);
        if(!graph[j]){
            graph[j] = new Set();
        }
        graph[j].add(i);
    }
    let max = 0;
    for(let i=0; i<n;i++) {
        for(let j=i+1; j<n;j++) {
            let curr = 0;
            if(graph[j] && graph[j].has(i)){
                curr--;
            }
            let size1 = graph[i] ? graph[i].size : 0;
            let size2 = graph[j] ? graph[j].size : 0;
            curr += size1 + size2;
            max = Math.max(curr, max);
        }
    }
    return max;
};