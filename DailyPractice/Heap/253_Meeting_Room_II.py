import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort()
        freeroom = []
        heapq.heappush(freeroom, intervals[0][1])
        for interval in intervals[1:]:
            if freeroom[0] <= interval[0]:
                heapq.heappop(freeroom)
            heapq.heappush(freeroom, interval[1])
        return len(freeroom)
