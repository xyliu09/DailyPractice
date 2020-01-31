import collections


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = collections.defaultdict(list)
        self.value = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append(timestamp)
        self.value[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.time[key], timestamp)

        return self.value[key][i - 1] if i else ''


        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)