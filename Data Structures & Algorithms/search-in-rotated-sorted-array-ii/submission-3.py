class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return True
            
            # if left half is sorted
            if nums[l] < nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            # if right half is sorted
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            # if nums[m] == nums[l] -> dont know for sure which half is sorted
            else:
                l += 1
        
        return False