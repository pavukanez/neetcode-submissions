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
        clones = {None: None}

        cur = head

        while cur:
            clone = Node(cur.val)
            clones[cur] = clone
            cur = cur.next

        cur = head

        while cur:
            clone = clones[cur]
            clone.next = clones[cur.next]
            clone.random = clones[cur.random]
            cur = cur.next

        return clones[head]