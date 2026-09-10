class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i: set() for i in range(1, n + 1)}

        for p1, p2 in trust:
            graph[p1].add(p2)
        
        judge = -1
        for key, val in graph.items():
            if len(val) == 0:
                judge = key
        
        if judge == -1: 
            return -1
        
        for person, people in graph.items():
            if person == judge:
                continue
            if judge not in people:
                return -1
        
        return judge