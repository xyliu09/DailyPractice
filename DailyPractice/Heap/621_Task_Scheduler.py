import collections
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = collections.Counter(tasks)
        queue = []
        for _, count in table.items():
            heapq.heappush(queue, -count)
        res = 0
        while queue:
            t = []
            cnt = 0
            for _ in range(n+1):
                if queue:
                    t.append(heapq.heappop(queue))
                    cnt += 1
            for count in t:
                if count + 1 < 0:
                    heapq.heappush(queue, count + 1)
            res += cnt if not queue else n+1
        return res