class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or newInterval[0] > intervals[-1][-1]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        for i in range(0, len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                for j in range(i, len(intervals)):
                    if newInterval[1] < intervals[j][0]:
                        return intervals[:i] + [[min(newInterval[0], intervals[i][0]),
                                                 max(intervals[j - 1][1], newInterval[1])]] + intervals[j:]
                    elif newInterval[1] <= intervals[j][1]:
                        return intervals[:i] + [[min(newInterval[0], intervals[i][0]), intervals[j][1]]] + intervals[
                                                                                                           j + 1:]
                return intervals[:i] + [[min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[-1][1])]]