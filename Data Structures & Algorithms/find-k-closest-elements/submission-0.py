class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = 0
        cur = float('inf')

        for i, num in enumerate(arr):
            if abs(num - x) < abs(cur - x):
                idx = i
                cur = num
        
        res = [cur]
        k -= 1

        l, r = idx - 1, idx + 1

        while k > 0:
            left = arr[l] if l > 0 else float('inf')
            right = arr[r] if r < len(arr) else float('inf')

            if abs(left - x) <= abs(right -x):
                res.append(left)
                l -= 1
            else:
                res.append(right)
                r += 1
            k -= 1
        
        return sorted(res)
            