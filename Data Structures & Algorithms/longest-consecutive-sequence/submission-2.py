class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            if (num - 1) in seen:
                continue
            
            cur = num
            count = 0
            while cur in seen:
                count += 1
                cur += 1
            res = max(res, count)
        
        return res
            