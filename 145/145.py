# 145. Binary Tree Postorder Traversal

# iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[(root,0)]
        res=[]
        while stack:
            node, num = stack.pop()
            if num==1:
                res.append(node.val)
            else:
                stack.append((node, 1))
                if node.right:
                    stack.append((node.right, 0))
                if node.left:
                    stack.append((node.left,0))
        return res
