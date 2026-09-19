class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = -1
        c1 = c2 = 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
            elif c2 == 0:
                n2 = num
            else:
                c1 -= 1
                c2 -= 1
        
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            if num == n2:
                c2 += 1
        
        res = []
        if c1 // 3 > 0:
            res.append(n1)
        if c2 // 3 > 0:
            res.append(n2)

        return res