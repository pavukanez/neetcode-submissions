class Node:

    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = Node(0)
        self.rear = Node(0)
        self.count = 0
        self.k = k
        
        self.front.next = self.rear
        self.rear.prev = self.front

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        
        node = Node(value)

        prev_rear = self.rear.prev
        prev_rear.next = node
        node.prev = prev_rear

        self.rear.prev = node
        node.next = self.rear

        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        next_next_front = self.front.next.next
        next_next_front.prev = self.front
        self.front.next = next_next_front

        self.count -= 1
        
        return True
        

    def Front(self) -> int:
        return self.front.next.val if self.count > 0 else -1
        

    def Rear(self) -> int:
        return self.rear.prev.val if self.count > 0 else -1
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()