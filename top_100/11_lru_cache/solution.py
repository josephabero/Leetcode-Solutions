"""
LRU Cache
https://leetcode.com/problems/lru-cache/
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Initialize linked list
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        node.prev, node.next = self.head, self.head.next
        node.prev.next = node.next.prev = node

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        node = None
        if key in self.cache:
            node = self.cache[key]

            # Insert as most recently used
            self.remove(node)
            self.insert(node)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        # Update cache
        node = Node(key, value)
        self.cache[key] = node

        # Insert as most recently used
        self.insert(node)

        # Delete if needed
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
