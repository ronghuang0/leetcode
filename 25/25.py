# 25. Reverse Nodes in k-Group

# iterative
# time: O(n)
# space: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        def getKth(node):
            count = 0
            while node and count < k:
                node = node.next
                count+=1
            return node
        
        dummy = ListNode(0, head)
        curr = dummy
    
        while True:
            beforeGroup = curr
            kth = getKth(curr)
            if not kth:
                break
            prev =kth.next
            count = 0
            curr = curr.next
            while count<k:
                temp=curr.next
                curr.next = prev
                prev = curr
                curr=temp
                count+=1
            curr = beforeGroup.next
            beforeGroup.next = kth
        return dummy.next


# recursive
# time: O(n)
# space: O(n/k) - the call stack reaches a size of n/k since we process k nodes each time
class Solution:
    def reverseKGroup(self, head, k: int):
        def reverse(head, k):
            curr = head
            prev = None
            while k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k-=1
            return prev
        
        count = 0
        node = head
        while count < k:
            if not node:
                return head
            node = node.next
            count+=1
        newHead = reverse(head, k)
        head.next = self.reverseKGroup(node, k)
        return newHead