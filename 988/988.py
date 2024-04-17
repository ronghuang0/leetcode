# 988. Smallest String Starting from Leaf

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res=None
        def dfs(curr, node):
            curr=chr(ord('a')+node.val)+curr
            if not node.left and not node.right:
                nonlocal res
                if not res or curr<res:
                    res=curr
            if node.left:
                dfs(curr, node.left)
            if node.right:
                dfs(curr,node.right)
        dfs('', root)
        return res