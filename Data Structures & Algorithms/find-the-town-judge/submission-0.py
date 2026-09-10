class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for p1, p2 in trust:
            graph[p1].append(p2)
        
        for key, val in graph.items():
            if len(val) == 0:
                return key
        return -1