# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        for _ in range(left - 1):
            p1 = p1.next
            head = head.next

        p2, next = None, None
        for _ in range(right - left + 1):
            next = head.next
            head.next = p2
            p2 = head
            head = next
        
        p3 = head

        p1.next = p2

        for _ in range(right - left):
            p2 = p2.next
        
        p2.next = p3

        return dummy.next
