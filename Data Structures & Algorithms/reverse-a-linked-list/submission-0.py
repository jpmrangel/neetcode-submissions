# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur is None:
            return None

        prv, nxt = None, cur.next
        if not nxt:
            return cur

        while cur:
            cur.next = prv
            prv = cur
            cur = nxt
            if cur.next:
                nxt = cur.next
            else:
                cur.next = prv
                break
        
        return cur

