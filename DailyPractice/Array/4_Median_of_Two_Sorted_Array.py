class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if (n1 + n2) % 2 != 0:
            return self.findMedian(nums1, nums2, 0, 0, (n1 + n2 + 1) // 2)
        return float(self.findMedian(nums1, nums2, 0, 0, (n1 + n2) / 2) + self.findMedian(nums1, nums2, 0, 0,
                                                                                          (n1 + n2) / 2 + 1)) / 2

    def findMedian(self, nums1, nums2, h1, h2, n):
        if h1 == len(nums1):
            return nums2[h2 + n - 1]
        if h2 == len(nums2):
            return nums1[h1 + n - 1]
        if n == 1:
            return min(nums1[h1], nums2[h2])
        m = min(len(nums1) - h1, len(nums2) - h2, n // 2)
        if nums1[h1 + m - 1] < nums2[h2 + m - 1]:
            return self.findMedian(nums1, nums2, h1 + m, h2, n - m)
        return self.findMedian(nums1, nums2, h1, h2 + m, n - m)