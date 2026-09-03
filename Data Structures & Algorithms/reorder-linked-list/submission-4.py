# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        slow, fast = head, head
        l1, l2 = head, head
        
        #two pointers to find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None

        if l2 is None:
            return None

        #reverse the second half
        prv, cur = None, l2
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        l2 = prv

        #merge them
        while l1 and l2:
            aux1 = l1.next
            aux2 = l2.next
            l1.next = l2
            l2.next = aux1
            
            l1 = aux1
            l2 = aux2
        
        if l2 is not None:
            l1.next = l2
        return None