class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            pace = l + (r - l) // 2

            time = 0

            for pile in piles:
                time += math.ceil(pile / pace)
            
            if time <= h:
                res = min(res, pace)
                r = pace - 1
            else:
                l = pace + 1
        return res