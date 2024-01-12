# 2385. Amount of Time for Binary Tree to Be Infected

# make a graph
from collections import defaultdict
class Solution:
    def amountOfTime(self, root, start: int) -> int:
        map = defaultdict(list)
        def traverse(node):
            if node.right:
                map[node.val].append(node.right.val)
                map[node.right.val].append(node.val)
                traverse(node.right)
            if node.left:
                map[node.left.val].append(node.val)
                map[node.val].append(node.left.val)
                traverse(node.left)
        traverse(root)
        stack = [start]
        seen = set()
        seen.add(start)
        count = 0
        while stack:
            next = []
            for v in stack:
                for n in map[v]:
                    if n not in seen:
                        next.append(n)
                        seen.add(n)
            count+=1
            stack = next
        return count-1

# one pass
# four cases:
# 1) root is null
# 2) root is start
# 3) tree doesn't contain start
# 4) tree does contain start

class Solution:
    def __init__(self):
        self.result = 0
    def traverse(self, root, start):
        if root is None:
            return 0
        depth = 0
        leftDepth = self.traverse(root.left, start)
        rightDepth = self.traverse(root.right, start)
        if root.val == start:
            self.result = max(leftDepth, rightDepth)
            depth=-1
        elif leftDepth >=0 and rightDepth >=0:
            depth=max(leftDepth, rightDepth)+1
        else:
            depth = min(leftDepth, rightDepth)-1
            self.result = max(self.result, abs(leftDepth) + abs(rightDepth))
        return depth
    def amountOfTime(self, root, start):
        self.traverse(root, start)
        return self.result