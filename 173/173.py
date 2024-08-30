# 173. Binary Seach Tree Iterator

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        curr=root
        while curr:
            self.stack.append(curr)
            curr=curr.left


    def next(self) -> int:
        res = self.stack[-1]
        curr = self.stack.pop()
        if curr.right:
            curr=curr.right
            while curr:
                self.stack.append(curr)
                curr=curr.left
        return res.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False