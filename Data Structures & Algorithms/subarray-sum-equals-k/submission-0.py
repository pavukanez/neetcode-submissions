class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0

        prefixCount = {0: 1}

        for num in nums:
            curSum += num

            diff = curSum - k

            if diff in prefixCount:
                res += prefixCount[diff]
            
            prefixCount[curSum] = 1 + prefixCount.get(curSum, 0)

        return res