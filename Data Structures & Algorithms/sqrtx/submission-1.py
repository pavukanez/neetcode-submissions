class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, math.ceil(x / 2)
        res = 0

        while l <= r:
            m = l + (r - l) // 2

            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res