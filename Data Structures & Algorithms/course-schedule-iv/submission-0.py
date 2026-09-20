class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        courseMap = {i: [] for i in range(numCourses)}

        for pre, course in prerequisites:
            courseMap[course].append(pre)
        

        def dfs(num, target):
            if num == target:
                return True

            for pre in courseMap[num]:
                found = dfs(pre, target)
                if found:
                    return True
            return False
        
        for pre, course in queries:
            res.append(dfs(course, pre))
        
        return res