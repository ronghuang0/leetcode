var tree2str = function(root) {
    let dfs = (node)=>{
        if(node === null){
            return '';
        }
        let res = String(node.val);
        let left = dfs(node.left);
        let right = dfs(node.right);
        if(node.left===null && node.right===null){
            return res;
        }
        if(node.left === null){
            return res+'()'+ '('+right+')'
        }
        if(node.right === null){
            return res + '('+left+')'
        }
        return res+'('+left+')'+ '('+right+')'

    }
    return dfs(root);
};