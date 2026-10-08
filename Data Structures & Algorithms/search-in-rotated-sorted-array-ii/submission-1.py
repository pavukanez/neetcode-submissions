class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1
        
        # Pass 1: Find the rotation pivot (index of the minimum element)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1  # Handle duplicates
                
        pivot = l
        
        # Determine which sorted half the target belongs to
        if pivot < n and nums[pivot] <= target <= nums[n - 1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1
            
        # Pass 2: Standard binary search in the chosen range
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return False
