class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            i = l

            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]

            if i > k:
                return quickSelect(l, i - 1)
            elif i < k:
                return quickSelect(i + 1, r)
            else:
                return nums[i]
        
        return quickSelect(0, len(nums) - 1)
