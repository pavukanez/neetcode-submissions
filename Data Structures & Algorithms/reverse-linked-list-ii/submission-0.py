# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, next = None, None

        while left <= right:
            next = head.next
            head.next = prev
            prev = head
            head = next

            left += 1
        
        dummy = prev
        while prev.next:
            prev = prev.next
        prev.next = head

        return dummy
