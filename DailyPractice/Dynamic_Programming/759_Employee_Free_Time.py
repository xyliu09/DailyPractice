"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        time = sorted([t for s in schedule for t in s], key = lambda x:x.start)
        busy = []
        for i in range(len(time)):
            if not busy or busy[-1].end < time[i].start:
                busy.append(time[i])
            else:
                busy[-1].end = max(busy[-1].end, time[i].end)
        ans = []
        for i in range(1, len(busy)):
            ans.append(Interval(busy[i-1].end, busy[i].start))
        return ans
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        time = sorted([t for s in schedule for t in s], key = lambda x:x.start)
        ans, end = [] , time[0].end
        for i in time[1:]:
            if i.start > end:
                ans.append(Interval(end, i.start))
            end = max(end, i.end)
        return ans