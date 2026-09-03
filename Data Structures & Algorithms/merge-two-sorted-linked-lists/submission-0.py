# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2
        if a is None:
            return b
        if b is None:
            return a

        aux, res = list1, list1
        if a.val <= b.val:
            res = a
            aux = res
            a = a.next
        else:
            res = b
            aux = res
            b = b.next

        while a and b:
            if a.val <= b.val:
                aux.next = a
                aux = a
                a = a.next
            else:
                aux.next = b
                aux = b
                b = b.next
        
        if a is None:
            aux.next = b
        else:
            aux.next = a

        return res

                