# 623. Add One Row to Tree

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            t = TreeNode(val)
            t.left=root
            return t
        currDepth=1
        level = [root]
        while currDepth<depth-1:
            next = []
            for node in level:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            currDepth+=1
            level=next
        for node in level:
            t1 = TreeNode(val)
            t2 = TreeNode(val)
            node.left, t1.left=t1, node.left
            node.right, t2.right=t2, node.right
        return root