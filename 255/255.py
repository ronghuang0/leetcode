# 255. Verify Preorder Sequence in Binary Search Tree

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        currMin = 0
        for val in preorder:
            if val < currMin:
                return False
            while stack and val>stack[-1]:
                currMin = stack[-1]
                stack.pop()
            stack.append(val)
        return True