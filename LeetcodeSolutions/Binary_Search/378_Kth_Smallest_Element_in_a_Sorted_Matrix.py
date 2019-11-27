import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, high = matrix[0][0], matrix[-1][-1]
        while lo < high:
            mid = (lo+high)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                high = mid
        return lo