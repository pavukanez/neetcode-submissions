class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(idx, subset):
            
            for j in range(idx, len(nums)):
                subset.append(nums[j])

                res.append(subset.copy())

                dfs(j + 1, subset)

                subset.pop()

        dfs(0, [])

        return res