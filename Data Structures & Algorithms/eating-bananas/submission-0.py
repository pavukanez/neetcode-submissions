class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        paces = [i for i in range(1, max(piles))]

        l, r = 0, len(paces) - 1
        res = max(piles)

        while l <= r:
            m = l + (r - l) // 2

            pace = paces[m]
            time = 0

            for pile in piles:
                time += math.ceil(pile / pace)
            
            if time <= h:
                res = min(res, pace)
                r = m - 1
            else:
                l = m + 1
        return res