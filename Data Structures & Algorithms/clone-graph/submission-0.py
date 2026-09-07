"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.seen = {}

        def dfs(node):
            if node in self.seen:
                return self.seen[node]
            
            clone = Node(node.val)
            self.seen[node] = clone

            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                clone.neighbors.append(clone_neighbor)
            
            return clone
        
        return dfs(node)