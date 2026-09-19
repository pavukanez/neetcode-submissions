class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        res, count = -1, 0

        for num in nums:
            if num == res:
                count += 1
            elif count == 0:
                count = 1
                res = num
            else:
                count -= 1
        
        return res
        