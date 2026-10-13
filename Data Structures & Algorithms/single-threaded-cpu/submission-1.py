class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []

        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x: x[0])

        idx = 0
        time = tasks[0][0]
        res = []

        while idx < len(tasks) or avail:
            while idx < len(tasks) and time >= tasks[idx][0]:
                _, processTime, i = tasks[idx]
                heapq.heappush(avail, (processTime, i))
                idx += 1
            
            if avail:
                processTime, i = heapq.heappop(avail)
                time += processTime
                res.append(i)
            else:
                time = tasks[idx][0]
        
        return res

