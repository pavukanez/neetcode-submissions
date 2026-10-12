class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maxHeap = [count for count in counter.values()]
        heapq.heapify_max(maxHeap)

        q = deque()
        res = 0

        while maxHeap or q:
            res += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count > 0:
                    q.append((count, res + n))
            
            if q and q[0][1] == res:
                count = q.popleft()[0]
                heapq.heappush_max(maxHeap, count)
            
        return res

        