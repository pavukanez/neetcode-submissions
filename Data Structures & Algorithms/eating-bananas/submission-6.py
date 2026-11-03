class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            pace = l + (r - l) // 2

            time = sum(math.ceil(pile / pace) for pile in piles)

            if time <= h:
                res = pace
                r = pace - 1
            else:
                l = pace + 1

        return res