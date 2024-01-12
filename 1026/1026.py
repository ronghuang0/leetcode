# Maximum Difference Between Node and Ancestor

# go through each node and keep track of max/min. See if node.val-max/min results in a new max diff
class Solution:
    def maxAncestorDiff(self, root) -> int:
        self.diff = 0
        def helper(node, maximum, minimum):
            if node is None:
                return
            self.diff = max(self.diff, abs(node.val-maximum), abs(node.val-minimum))
            maximum = max(node.val, maximum)
            minimum = min(node.val, minimum)
            helper(node.left, maximum, minimum)
            helper(node.right, maximum, minimum)
        helper(root, root.val, root.val)
        return self.diff

# notice that the number of paths through the tree is same as number of leafs
# at any point we can just take max-min
class Solution:
    def maxAncestorDiff(self, root) -> int:
        self.diff = 0
        def helper(node, maximum, minimum):
            if node is None:
                return
            maximum = max(node.val, maximum)
            minimum = min(node.val, minimum)
            self.diff = max(self.diff, abs(maximum-minimum))
            helper(node.left, maximum, minimum)
            helper(node.right, maximum, minimum)
        helper(root, root.val, root.val)
        return self.diff