class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        while intervals:
            element = intervals.pop(0)
            if not res or (res and res[-1][-1] < element[0]):
                res.append(element)
            else:
                res[-1][-1] = max(element[1], res[-1][-1])
        return res