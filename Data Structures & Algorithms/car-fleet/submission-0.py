class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(reverse=True)

        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]
            
            # if stack empty -> push time to stack
            if not stack:
                stack.append(time)
                continue
            if stack and time <= stack[-1]:
                continue
            if stack and time > stack[-1]:
                stack.append(time)
                continue
        return len(stack)
            # if stack not empty and time <= top stack -> dont push

            # if stack not empty and time > top stack -> push
