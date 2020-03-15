class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = sumS = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(h, s)
            sumS += s
            if len(h) > k:
                sumS -= heapq.heappop(h)
            res = max(res, sumS * e)
        return res % (10 ** 9 + 7)


