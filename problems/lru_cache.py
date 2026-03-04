#Bruteforce way by using a list which time complexity will be O(n) for put and get
#space complexity will be O(capacity)
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache ={}
#         self.track = []

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.track.remove(key)
#         self.track.append(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.track.remove(key)
#             self.track.append(key)
#         else:
#             self.cache[key] = value
#             self.track.append(key)
#             if len(self.cache) > self.capacity:
#                 lru = self.track.pop(0)
#                 del self.cache[lru]


#OPTIMAL WAY BY USING A BOUBLY LINKED LIST

#create a node class to us to creater the doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        #create a hashmap and the doubly linked list
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #connecting the linked list
        self.left.next = self.right
        self.right.prev = self.left

    #helper functions to help remove and insert nodes in a linked list
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        #if it exists, update it to be the most recently used
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        #if the key exists, we remove and reinster it
        if key in self.cache:
            self.remove(self.cache[key])
        
        #insert the node to the linked list and cache
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]



if __name__ == "__main__":
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    out = []
    obj = None

    for op, a in zip(ops, args):
        if op == "LRUCache":
            obj = LRUCache(a[0])
            out.append(None)
        elif op == "put":
            obj.put(a[0], a[1])
            out.append(None)
        elif op == "get":
            out.append(obj.get(a[0]))

    print(out)
    # expected: [None, None, None, 1, None, -1, None, -1, 3, 4]