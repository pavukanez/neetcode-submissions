class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = []

        for c, count in counter.items():
            heapq.heappush_max(maxHeap, (count, c))
        
        res = ""

        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            count, c = heapq.heappop_max(maxHeap)
            res += c
            
            if prev:
                heapq.heappush_max(maxHeap, prev)
                prev = None

            if count - 1 > 0:
                prev = (count - 1, c)

        return res