class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = []
        trips.sort(key=lambda x: x[1])

        cur = capacity

        for count, fromLoc, toLoc in trips:
            if not car:
                cur = capacity - count
                heapq.heappush(car, (toLoc, count))
            else:
                # offboard as many as possible
                while car and fromLoc >= car[0][0]:
                    _, oldCount = heapq.heappop(car)
                    cur += oldCount

                # onboard new passenger
                heapq.heappush(car, (toLoc, count))
                cur -= count
                
                if cur < 0:
                    return False # overboard
                else:
                    heapq.heappush(car, (toLoc, count))
                        
        return True