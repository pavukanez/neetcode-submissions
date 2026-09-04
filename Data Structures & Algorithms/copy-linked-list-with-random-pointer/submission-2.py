"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        clones = {}

        cur = head

        while cur:
            clone = Node(cur.val)
            clones[cur] = clone
            cur = cur.next

        cur = head

        while cur:
            clone = clones[cur]
            if cur.next:
                clone.next = clones[cur.next]
            if cur.random:
                clone.random = clones[cur.random]
            cur = cur.next

        return clones[head]