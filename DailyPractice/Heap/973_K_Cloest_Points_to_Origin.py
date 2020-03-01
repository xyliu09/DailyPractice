import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for x,y in points:
            distance = -(x**2+ y**2)
            if len(heap) == K:
                heapq.heappushpop(heap, (distance, x,y))
            else:
                heapq.heappush(heap, (distance, x,y))
        return [(x,y) for (distance, x, y) in heap]