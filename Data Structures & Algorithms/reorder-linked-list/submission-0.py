# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        head2 = self.reverse(head2)

        while head and head2:
            next1 = head.next
            next2 = head2.next

            head.next = head2
            head2.next = next1

            head = next1
            head2 = next2
    
    def reverse(self, head) -> ListNode:
        if not head:
            return None

        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev