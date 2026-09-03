# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = list1 if list1.val <= list2.val else list2

        while list1 and list2:
            if list1.val <= list2.val:
                next = list1.next
                list1.next = list2
                list1 = next
            else:
                next = list2.next
                list2.next = list1
                list2 = next
        return res