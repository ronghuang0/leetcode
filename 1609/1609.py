#1609. Even Odd Tree

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        q = [root]
        while q:
            next = []
            prev = float('inf')
            if even:
                prev = float('-inf')
            for n in q:
                if even and (n.val <= prev or n.val%2==0):
                    return False
                if not even and (n.val>=prev or n.val%2==1):
                    return False
                prev = n.val
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            even = not even
            q = next
        return True
