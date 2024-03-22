# 1669. Merge In Between Linked Lists

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = list2
        tail2 = head2
        while tail2.next:
            tail2=tail2.next
        
        dummy=ListNode(None, list1)
        atB=dummy
        for i in range(0, b+1):
            atB=atB.next
        beforeA=dummy
        for i in range(0, a):
            beforeA=beforeA.next
        beforeA.next=head2
        tail2.next=atB.next
        return dummy.next