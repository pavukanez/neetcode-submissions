class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)
        curMax = curMaxCount = 0

        for num in nums:
            count[num] += 1
            if curMaxCount < count[num]:
                curMax = num
                curMaxCount = count[num]
        return curMax
        