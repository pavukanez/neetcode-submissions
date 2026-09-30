class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r in range(len(nums)):
            next = nums[r + 1] if r < len(nums) - 1 else nums[r] + 1
            if nums[r] != next:
                nums[l] = nums[r]
                l += 1

        nums = nums[:l]

        return l

