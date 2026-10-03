class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        window = set()
        
        for i in range(k):
            window.add(nums[i])
        
        if len(window) != k:
            return True
        
        l = 0
        for r in range(k, len(nums)):
            if nums[r] in window:
                return True
            window.remove(nums[l])
            l += 1
            window.add(nums[r])
        
        return False