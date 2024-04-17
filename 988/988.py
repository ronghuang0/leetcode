# 988. Smallest String Starting from Leaf

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res=None
        def dfs(curr, node):
            char = chr(ord('a')+int(node.val))
            curr+=char
            if not node.left and not node.right:
                nonlocal res
                if not res:
                    res=curr[::-1]
                else:
                    res=min(res, curr[::-1])
            if node.left:
                dfs(curr, node.left)
            if node.right:
                dfs(curr,node.right)
        dfs('', root)
        return res