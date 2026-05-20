class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            # 3,4,5,6 [7]
            # 3:0
            # 
            if diff in seen:
                return [seen.get(diff), i]
            seen[num] = i
        return []
