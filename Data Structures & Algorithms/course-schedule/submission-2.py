class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}

        for i in range(numCourses):
            courseMap[i] = []

        for course, pre in prerequisites:
            courseMap[course].append(pre)
        
        status = [0 for _ in range(numCourses)]
        
        def dfs(course):
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True
            
            status[course] = 1

            pres = courseMap[course]
            for pre in pres:
                if not dfs(pre):
                    return False
            
            status[course] = 2

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
