class Node(object):

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.data = {}
        self.order = Node()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.data:
            return -1
        else:
            self.update_order(key)
            return self.data[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass

    def update(self, key):
        # update key to be the most recently used elements.
        head = self.order
        if head.val == key:
            return
        else:
            newNode = Node(key)
            while head.val!=key:
                head = head.next
            head.prev.next = head.next
            newNode.next = self.order
            self.order = newNode




our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
