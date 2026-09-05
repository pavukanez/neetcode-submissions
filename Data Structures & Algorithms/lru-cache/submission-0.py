class Node:
    
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node 
         
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key] 
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
         

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            target = self.left.next
            self.remove(target)
            del self.cache[target.key]

