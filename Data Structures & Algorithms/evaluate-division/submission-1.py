class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, equation in enumerate(equations):
            u, v = equation
            adj[u].append((v, values[i]))
            adj[v].append((u, 1 / values[i]))
        
        def dfs(src, target, seen):
            if src not in adj or target not in adj:
                return -1
            
            if src == target:
                return 1
            
            seen.add(src)

            for nei, wei in adj[src]:
                if nei not in seen:
                    res = dfs(nei, target, seen)
                    if res != -1:
                        return wei * res
            return -1

        return [dfs(q[0], q[1], set()) for q in queries]