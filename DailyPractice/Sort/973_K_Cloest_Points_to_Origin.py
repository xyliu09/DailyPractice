import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        def helper(arr, l, r):

            pivot = arr[l]
            while l < r:
                while l < r and (arr[r][0] ** 2 + arr[r][1] ** 2) - (pivot[0] ** 2 + pivot[1] ** 2) >= 0:
                    r -= 1
                arr[l] = arr[r]
                while l < r and (arr[l][0] ** 2 + arr[l][1] ** 2) - (pivot[0] ** 2 + pivot[1] ** 2) <= 0:
                    l += 1
                arr[r] = arr[l]
            arr[l] = pivot
            return l

        l, r = 0, len(points) - 1
        while l <= r:
            mid = helper(points, l, r)
            if mid == K:
                break
            elif mid < K:
                l = mid + 1
            else:
                r = mid - 1
        return points[:K]