# 1457. Pseudo-Palindromic Paths in a Binary Tree

# recursive
# time: O(n)
# space: O(n) - height of the tree, worst case of all single child
class Solution:
    def pseudoPalindromicPaths (self, root):
        res = 0
        def dfs(node, path):
            if not node:
                return
            path = path ^ 1<<node.val
            if not node.right and not node.left:
                if path & (path-1) == 0:
                    nonlocal res
                    res+=1
                return
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, 0)
        return res

# iterative
# time: O(n)
# space: O(n) height of tree - worse case of all single child
class Solution:
    def pseudoPalindromicPaths (self, root):
        res = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            path = path ^ (1<<node.val)
            if not node.left and not node.right:
                if path & (path-1) == 0:
                    res+=1
            stack.append((node.left, path))
            stack.append((node.right, path))
        return res