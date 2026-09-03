# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        l1, slow, fast = head, head, head
        
        #two pointers to find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        if l2 is None:
            return
        slow.next = None

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
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2
        
        if l2 is not None:
            l1.next = l2
