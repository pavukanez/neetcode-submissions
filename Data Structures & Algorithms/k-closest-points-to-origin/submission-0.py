class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            x, y = point[0], point[1]
            dist = x ** 2 + y ** 2

            heapq.heappush_max(maxHeap, [dist, x, y])

            while len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        res = []
        while maxHeap:
            cur = heapq.heappop_max(maxHeap)

            res.append([cur[1], cur[2]])

        return res

