class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        res = 0

        while l <= r:
            if l == r:
                res += 1
                l += 1
            else:
                wL, wR = people[l], people[r]
                if wL + wR <= limit:
                    l += 1
                    r -= 1
                else:
                    if wR >= wL:
                        r -= 1
                    else:
                        l += 1
                res += 1
                
        return res