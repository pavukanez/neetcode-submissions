class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums) - 1
        l, r = 0, n - 1

        while l <= r:
            m = (r + l) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
            
        pivot = l
    
        if nums[pivot] <= target <= nums[n - 1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1
        
        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False