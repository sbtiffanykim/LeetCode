class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key] = self.cache.pop(key)  # to update its rank
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # to update its rank
            self.cache.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache.pop(next(iter(self.cache)))  # pop the LRU key

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)