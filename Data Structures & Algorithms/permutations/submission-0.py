class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, seen):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                
                path.append(nums[i])
                seen.add(nums[i])

                dfs(path, seen)

                num = path[-1]
                path.pop()
                seen.remove(num)
        
        dfs([], set())

        return res