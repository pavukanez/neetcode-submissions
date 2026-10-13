class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0: maxHeap.append((a, 'a', False))
        if b > 0: maxHeap.append((b, 'b', False))
        if c > 0: maxHeap.append((c, 'c', False))
        heapq.heapify_max(maxHeap)

        prev = None

        res = ""

        while maxHeap or prev:
            if not maxHeap and prev[0] > 0:
                return res
            
            count, c, used = heapq.heappop_max(maxHeap)
            res += c
            count -= 1

            if prev:
                heapq.heappush_max(maxHeap, (prev[0], prev[1], False))
                prev = None

            if count > 0:
                if used:
                    prev = (count, c)
                else:
                    heapq.heappush_max(maxHeap, (count, c, True))
        
        return res


