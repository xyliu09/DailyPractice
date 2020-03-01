class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        while intervals:
	        element = intervals.pop(0)
	        if not res or (res and element[0]> res[-1][-1]):
		        res.append(element)
	        else:
		        res[-1][-1] = max(element[1],res[-1][-1])
        return res