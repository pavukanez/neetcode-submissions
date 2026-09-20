class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courseMap = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            courseMap[v].append(u)

        preMap = {}

        def dfs(num):
            if num not in preMap:

                preMap[num] = set()
                for pre in courseMap[num]:
                    updated_pres = dfs(pre)
                    preMap[num].update(updated_pres)
                preMap[num].add(num)
            return preMap[num]


        for course in range(numCourses):
            dfs(course)
        
        res = []
        for u, v in queries:
            res.append(u in preMap[v])
        
        return res