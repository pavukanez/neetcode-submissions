class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i, equation in enumerate(equations):
            s1, s2 = equation

            graph[s1][s2] = values[i]
            graph[s2][s1] = 1 / values[i]

        res = []

        def dfs(s1, s2, seen):
            if s2 in graph[s1]:
                return graph[s1][s2]
            
            seen.add(s1)

            for nei, wei in graph[s1].items():
                if nei in seen:
                    continue
                a = dfs(s1, nei, seen)
                b = dfs(nei, s2, seen)
                if a != -1 and b != -1:
                    return a * b
            return -1

        return [dfs(q[0], q[1], set()) for q in queries]
            