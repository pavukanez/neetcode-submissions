class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter([c for c in s])
        maxHeap = []

        for c, count in counter.items():
            heapq.heappush_max(maxHeap, (count, c))
        
        res = ""

        q = deque()

        while maxHeap or q:
            if not maxHeap and q:
                return ""

            count, c = heapq.heappop_max(maxHeap)
            res += c
            
            if q:
                heapq.heappush_max(maxHeap, q.popleft())

            if count - 1 > 0:
                q.append((count - 1, c))

        return res