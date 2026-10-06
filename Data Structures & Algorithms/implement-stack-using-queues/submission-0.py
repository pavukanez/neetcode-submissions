class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.cur = 0        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.cur = x        

    def pop(self) -> int:
        res = 0
        curSize = len(self.queue1)
        for i in range(curSize):
            num = self.queue1.popleft()
            if i < curSize - 1:
                self.queue2.append(num)
            else:
                res = num
        
        for i in range(curSize - 1):
            self.cur = num = self.queue2.popleft()

            self.queue1.append(num)

        return res

    def top(self) -> int:
        return self.cur

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()