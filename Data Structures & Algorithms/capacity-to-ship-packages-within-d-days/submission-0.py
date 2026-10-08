class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (r + l) // 2

            total = 0
            count = 1
            for w in weights:
                if total + w > m:
                    total = w
                    count += 1
                else:
                    total += w
                
            if count <= days:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res