class Solution:
    import heapq
    def maxEvents(self, events: List[List[int]]) -> int:
        h = []
        res = 0
        A = sorted(events, reverse=True)
        day = 1
        while day <= 100000:
            while A and A[-1][0] <= day:
                heapq.heappush(h, A.pop()[1])
            while h and h[0] < day:
                print(h)
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                res += 1
            day += 1
        return res



