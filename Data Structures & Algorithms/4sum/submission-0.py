class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1

                while c < d:
                    cur = target - nums[a] - nums[b]
                    if nums[c] + nums[d] < cur:
                        c += 1
                    elif nums[c] + nums[d] > cur:
                        d -= 1
                    else:
                        res.add((nums[a], nums[b], nums[c], nums[d]))

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1

                        c += 1
                        d -= 1
        cur = []
        for quad in res:
            a,b,c,d = quad
            cur.append([a,b,c,d])
        
        return cur

