# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        def helper(num, node):
            num=num*10+node.val
            if not node.left and not node.right:
                nonlocal res
                res+=num
                return
            if node.left:           
                helper(num,node.left)
            if node.right:
                helper(num, node.right)
        helper(0,root)
        return res