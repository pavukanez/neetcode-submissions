class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        while l < r:
            m = (r + l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        pivot = l

        if nums[0] <= target <= nums[pivot - 1]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, n - 1
        
        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
        return -1