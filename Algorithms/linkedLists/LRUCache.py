# LRU Cache
# Link: https://leetcode.com/problems/lru-cache/description/

# The trick is to make a doubly linked list and have each
# value in the double linked list be accessible via
# hash table by knowing what the value is by mapping
# the value to it. 

class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.table = dict() # key: key, value: node
        self.head = Node()
        self.tail = Node()
        self.head.prev, self.tail.next = self.tail, self.head

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node):
        prev_node = self.head.prev
        next_node = self.head
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.table:
            self.delete(self.table[key])
            self.add(self.table[key])
            return self.table[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = value
            self.delete(node)
        else:
            node = Node(key, value)
            self.table[key] = node
            self.count += 1
        self.add(self.table[key])
        if self.count > self.capacity:
            delete_node = self.tail.next
            self.delete(delete_node)
            del self.table[delete_node.key]
            self.count -= 1
