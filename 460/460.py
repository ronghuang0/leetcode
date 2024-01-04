# 460. LFU Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.length = 0
        self.sentinel.next = self.sentinel.prev = self.sentinel
    def __len__(self):
        return self.length
    def append(self, node):
        first = self.sentinel.next
        self.sentinel.next = node
        first.prev = node
        node.prev=self.sentinel
        node.next=first
        self.length += 1
    def remove(self, node=None):
        if not node:
            node = self.sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -=1
        return node
    
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.least = 0
        self.keyToNode = {}
        self.freqToList = defaultdict(LinkedList)
    def update(self, key):
        node = self.keyToNode[key]
        self.freqToList[node.freq].remove(node)
        if self.least == node.freq and not self.freqToList[node.freq]:
            self.least +=1
        node.freq+=1
        self.freqToList[node.freq].append(node)
    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        self.update(key)
        return self.keyToNode[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.update(key)
            self.keyToNode[key].value = value
        else:
            if self.capacity == self.length:
                node = self.freqToList[self.least].remove()
                del self.keyToNode[node.key]
            else:
                self.length+=1
            n = Node(key, value)
            self.freqToList[1].append(n)
            self.keyToNode[key] = n
            self.least=1