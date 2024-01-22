# 1120. Maximum Average Subtree

# O(n) space (skewed tree) and time 
class Solution:
    def maximumAverageSubtree(self, root) -> float:
        res = 0
        def dfs(node):
            if node == None:
                return (0,0)
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            currSum = node.val+leftSum+rightSum
            currCount = 1 + leftCount+rightCount
            nonlocal res
            res = max(res, currSum/currCount)
            return (currSum, currCount)
        dfs(root)
        return res