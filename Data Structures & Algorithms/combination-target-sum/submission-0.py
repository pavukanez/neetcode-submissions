class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, comb, curSum):
            if curSum == target:
                res.append(comb.copy())
                return
            
            if curSum > target:
                return
            
            for j in range(idx, len(nums)):
                comb.append(nums[j])
                dfs(j, comb, curSum + nums[j])
                comb.pop()

        dfs(0, [], 0)

        return res