class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum, res = 0, float('inf')

        for r in range(len(nums)):
            curSum += nums[r]

            while curSum >= target: 
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1

        return res if res < float('inf') else 0