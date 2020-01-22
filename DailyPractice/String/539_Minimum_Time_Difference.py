class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted([int(time[:2])*60 + int(time[3:]) for time in timePoints])
        times.append(times[0] + 1440)
        return min(b-a for a, b in zip(times, times[1:]))