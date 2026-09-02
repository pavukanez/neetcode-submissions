class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, target, 0, len(nums) - 1)
        
    def dfs(self, nums, target, l, r):
        if l > r:
            return -1

        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.dfs(nums, target, l + 1, r)
        else:
            return self.dfs(nums, target, l, r - 1)
    
