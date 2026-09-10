class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        nodeMap = {i: [] for i in range(n)}

        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)

        def dfs(num):
            if num in visit:
                return

            visit.add(num)
            
            for neighbor in nodeMap[num]:
                dfs(neighbor)
        
        res = 0
        for num in range(n):
            if num in visit:
                continue
            
            dfs(num)
            res += 1
        
        return res