# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ogToCopy={}
        ogToCopy[None]=None
        def do(node):
            if node in ogToCopy:
                return ogToCopy[node]
            copy=Node(node.val)
            ogToCopy[node]=copy
            copy.next=do(node.next)
            copy.random=do(node.random)
            return copy
        return do(head)
            
