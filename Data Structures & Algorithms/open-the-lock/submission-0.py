class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if target == "0000":
            return 0
        if "0000" in seen:
            return -1
        
        queue = deque()
        queue.append(("0000", 0))

        def generate_next(lock):
            res = []

            for i in range(4):
                digit = int(lock[i])

                next_digit = (digit - 1) % 10
                next_lock = lock[:i] + str(next_digit) + lock[i+1:]

                if next_lock not in seen:
                    seen.add(next_lock)
                    res.append(next_lock)
            return res

        while queue:
            lock, turn = queue.popleft()
            if lock == target:
                return turn

            for next_lock in generate_next(lock):
                queue.append((next_lock, turn + 1))

        return -1
            

        

        
