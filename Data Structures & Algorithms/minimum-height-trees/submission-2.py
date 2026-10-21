class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj =[[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        degree = [0 for _ in range(n)]
        queue = deque()

        for node, neighbors in enumerate(adj):
            degree[node] = len(neighbors)
            if degree[node] == 1:
                queue.append(node)

        while queue:
            if n <= 2:
                return list(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1

                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        
        return [0]