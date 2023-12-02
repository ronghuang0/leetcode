// number of connected components in an undirected graph

let countComponents = (n, edges) =>{
    let map = {};
    edges.forEach(edge=>{
        let [u,v] = edge;
        if(map[u]){
            map[u].push(v);
        } else {
            map[u] = [v];
        }
        if(map[v]){
            map[v].push(u);
        } else {
            map[v]=[u];
        }
    });
    let visited = new Set();
    let dfs = (node)=>{
        visited.add(node);
        if(map[node] === undefined) {
            return;
        }
        for(let i=0;i<map[node].length;i++) {
            if(!visited.has(map[node][i])) {
                dfs(map[node][i])
            }
        }
    }
    let res = 0;
    for(let i=0; i<n;i++) {
        if(!visited.has(i)){
            res++;
            dfs(i);
        }
    }
    return res;
}


let countComponents2 = (n, edges) => {
    let parents = [...Array(n+1).keys()];
    let rank = Array(n).fill(1);
    let find = (n) => {
        let p = parents[n];
        while(p !== parents[p]){
            parents[p] = parents[parents[p]]
            p = parents[p];
        }
        return p;
    }
    let union = (n1, n2) => {
        let p1 = find(n1);
        let p2 = find(n2);
        if(p1 === p2) {
            return false;
        }

        if(rank[p1] > rank[p2]){
            parents[p2] = p1;
            rank[p1] += rank[p2];
        } else {
            parents[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
    }
    let res = n;
    for(let i=0; i<edges.length; i++) {
        let [u,v] = edges[i];
        if(union(u,v)){
            res--;
        }
    }
    return res;
}