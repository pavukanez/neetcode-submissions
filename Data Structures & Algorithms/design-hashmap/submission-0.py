class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.numMap = [Node(0, 0) for _ in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        cur = self.numMap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = Node(key, value)

    def get(self, key: int) -> int:
        cur = self.numMap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.numMap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
    def hash(self, key: int) -> int:
        return key % len(self.numMap)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)