import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict.pop(key)
            self.dict[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        elif key not in self.dict and len(self.dict) == self.capacity:
            k = next(iter(self.dict))
            del self.dict[k]
        self.dict[key] = value




        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)