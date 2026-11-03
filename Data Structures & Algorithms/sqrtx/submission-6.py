class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return 1

        l, r = 1, x // 2
        res = 0

        while l <= r:
            m = (r + l) // 2

            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res