class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        # 1,2,4,6
        # pre = [1,1,2,8]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        # 1,2,4,6
        # post = [48,24,6,1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        
        return res

        
        