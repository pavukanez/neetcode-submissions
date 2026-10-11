class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        count = len(stones)

        while count > 1:
            x, y = heapq.heappop(max_heap), heapq.heappop(max_heap)

            if x == y:
                count -= 2
                continue
            
            remain = -abs(x - y)
            heapq.heappush(max_heap, remain)
            count -= 1

        return -heapq.heappop(max_heap) if count == 1 else 0

