class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(idx, arr):
            nonlocal res

            cur = 0
            for num in arr:
                cur ^= num
            res += cur

            for j in range(idx, len(nums)):
                arr.append(nums[j])
                dfs(j + 1, arr)
                arr.pop()

        dfs(0, [])

        return res

        