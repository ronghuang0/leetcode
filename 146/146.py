# 146. LRU Cache

class ListNode:
    def __init__(self, key, val):
            self.key=key
            self.val=val
            self.prev=None
            self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head=ListNode(None, None)
        self.tail=ListNode(None, None)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert(self, node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            node.val=value
        else:
            if self.capacity == len(self.map):
                nodeToRemove = self.tail.prev
                del self.map[nodeToRemove.key]
                self.remove(nodeToRemove)
            node = ListNode(key, value)
            self.insert(node)
            self.map[key] = node
            