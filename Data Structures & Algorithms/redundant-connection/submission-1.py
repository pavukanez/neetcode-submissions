class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()
        cycle = set()

        cycleStart = -1

        nodeMap = {i: [] for i in range(1, len(edges) + 1)}
        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)


        def has_cycle(node, prev):
            nonlocal cycleStart

            if node in visit:
                cycleStart = node
                return True
            
            visit.add(node)
            for neighbor in nodeMap[node]:
                if neighbor == prev:
                    continue
                if has_cycle(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)

                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False
        
        has_cycle(1, -1)

        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if u in cycle and v in cycle:
                return [u, v]
        
        return []