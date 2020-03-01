class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)

        while start <= end:
            partitionx = (start + end) // 2
            partitiony = (len(nums1) + len(nums2) + 1) / 2 - partitionx

            maxleftX = - sys.maxint - 1 if partitionx == 0 else nums1[partitionx - 1]
            minrightX = sys.maxint if partitionx == len(nums1) else nums1[partitionx]
            maxleftY = - sys.maxint - 1 if partitiony == 0 else nums2[partitiony - 1]
            minrightY = sys.maxint if partitiony == len(nums2) else nums2[partitiony]

            if maxleftX <= minrightY and maxleftY <= minrightX:
                return max(maxleftX, maxleftY) if (len(nums1) + len(nums2)) % 2 else float(
                    max(maxleftX, maxleftY) + min(minrightX, minrightY)) / 2
            elif maxleftX > minrightY:
                end -= 1
            else:
                start += 1