# 2196. Create Binary Tree From Descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap={}
        children=set()
        for p, c, left in descriptions:
            children.add(c)
            if not p in nodeMap:
                nodeMap[p]=TreeNode(p)
            if not c in nodeMap:
                nodeMap[c]=TreeNode(c)
            if left:
                nodeMap[p].left=nodeMap[c]
            else:
                nodeMap[p].right=nodeMap[c]
        for node in nodeMap:
            if node not in children:
                return nodeMap[node]

