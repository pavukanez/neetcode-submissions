class Node:
    
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.seen = [Node(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.seen[key % len(self.seen)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        cur = self.seen[key % len(self.seen)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.seen[key % len(self.seen)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)