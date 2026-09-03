class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            pace = l + (r - l) // 2

            time = sum(math.ceil(pile / pace) for pile in piles)

            if time <= h:
                r = pace
            else:
                l = pace + 1
        return l