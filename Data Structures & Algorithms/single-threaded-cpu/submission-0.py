class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pending = []

        for i, (enqueueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))

        time = 0
        res = []

        while avail or pending:
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)

                heapq.heappush(avail, (processTime, i))

            if not avail: 
                time = pending[0][0]
                continue

            processTime, i = heapq.heappop(avail)
            time += processTime
            res.append(i)

        return res