class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            other = target - num

            if other in seen:
                return [seen.get(other), i]
            seen[num] = i
        
        return [0, 1]