class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(idx, subset):
            nonlocal res

            cur = 0
            for num in subset:
                cur ^= num
            res += cur

            for j in range(idx, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()

        dfs(0, [])

        return res

        