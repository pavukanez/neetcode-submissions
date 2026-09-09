class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}

        for i in range(numCourses):
            courseMap[i] = []

        for course, pre in prerequisites:
            courseMap[course].append(pre)
        
        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            visiting.add(course)

            pres = courseMap[course]
            for pre in pres:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)

            visited.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
