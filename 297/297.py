# 297. Serialize and Deserialize Binary Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# dfs
# O(n) space and time
class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append('n')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        
    def deserialize(self, data):
        arr = data.split(',') 
        index = 0
        def dfs():
            nonlocal index
            if arr[index] == 'n':
                index+=1
                return None
            node = TreeNode(arr[index])
            index+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()