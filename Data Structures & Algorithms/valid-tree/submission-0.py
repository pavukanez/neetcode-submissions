class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        nodeMap = {i: [] for i in range(n)}

        for node1, node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            back_to_parent_already = False
            for child in nodeMap[node]:
                if child == prev:
                    if back_to_parent_already:
                        return False
                    back_to_parent_already = True
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n

        