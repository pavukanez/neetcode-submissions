class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        def merge(left_arr, right_arr):
            res = []
            i, j = 0, 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    res.append(left_arr[i])
                    i += 1
                else:
                    res.append(right_arr[j])
                    j += 1

            res.extend(left_half[i:])
            res.extend(right_half[j:])

            return res

        return merge(left_half, right_half)
