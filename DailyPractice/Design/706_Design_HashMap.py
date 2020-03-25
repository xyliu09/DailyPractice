class LinkNode:
    def __init__(self, key, value):
        self.pair = [key, value]
        self.next = None


class MyHashMap:
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [['None' for _ in range(1000)] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.bucket[key%1000][key//1000] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        value = self.bucket[key%1000][key//1000]
        return -1 if value == 'None' else value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.bucket[key%1000][key//1000] = 'None'
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.bucket = [None] * 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashKey = key % 1000
        if not self.bucket[hashKey]:
            self.bucket[hashKey] = LinkNode(key, value)
        else:
            node = self.bucket[hashKey]
            while node:
                if node.pair[0] == key:
                    node.pair[1] = value
                    return
                if not node.next:
                    node.next = LinkNode(key, value)
                node = node.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashKey = key % 1000
        if self.bucket[hashKey]:
            node = self.bucket[hashKey]
            while node:
                if node.pair[0] == key:
                    return node.pair[1]
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = key % 1000
        prev = node = self.bucket[hashKey]
        if not node: return
        if node.pair[0] == key:
            self.bucket[hashKey] = node.next
        else:
            node = node.next
            while node:
                if node.pair[0] == key:
                    prev.next = node.next
                    break
                else:
                    prev, node = prev.next, node.next