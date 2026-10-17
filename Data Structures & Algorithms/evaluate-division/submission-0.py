class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        degrees = defaultdict(int)
        dag = defaultdict(list)

        for i, equation in enumerate(equations):
            s1, s2 = equation[0], equation[1]

            degrees[(s1, s2)] = values[i]
            degrees[(s2, s1)] = 1 / values[i]

            dag[s1].append(s2)
            dag[s2].append(s1)

        res = []

        def dfs(s1, s2, seen):
            if (s1, s2) in degrees:
                return degrees[(s1, s2)]
            
            seen.add(s1)

            for nei in dag[s1]:
                if nei in seen:
                    continue
                a = dfs(s1, nei, seen)
                b = dfs(nei, s2, seen)
                if a != -1 and b != -1:
                    return a * b
            return -1

        for query in queries:
            s1, s2 = query[0], query[1]
            res.append(dfs(s1, s2, set()))
        
        return res
            