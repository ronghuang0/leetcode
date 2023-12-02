
// i * (2i-1)
// think of this as placing the P in the front. After we do that the D has 2i-1 places to be placed.
// for every P we place that means there are 2i-1 possibilities. 




// think of this as placing the P in the front. We can choose from P available so it's P*dfs(p-1, d)
// this of this as placing the D in the front. only (d-p) of the d's can be put in front atm so it's (d-p)*dfs(p,d-1)
// compared to the method above we are placing P and D one at a time rather than P and D together.