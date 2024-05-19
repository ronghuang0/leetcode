# 979. Distribute Coins in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        total=0
        def dfs(node):
            if not node:
                return 0 
            netLeft=dfs(node.left)
            netRight=dfs(node.right)
            nonlocal total
            total+=abs(netLeft)+abs(netRight)
            return netLeft+netRight+node.val-1
        dfs(root)
        return total