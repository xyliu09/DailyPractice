class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        a, b = collections.Counter(nums1), collections.Counter(nums2)
        return list((a&b).elements())
        '''

        class Solution(object):
            def intersect(self, nums1, nums2):
                """
                :type nums1: List[int]
                :type nums2: List[int]
                :rtype: List[int]
                """
                nums1.sort(), nums2.sort()
                if len(nums1) > len(nums2):
                    nums1, nums2 = nums2, nums1
                p1, p2, res = 0, 0, []
                while p1 < len(nums1) and p2 < len(nums2):
                    while p1 < len(nums1) and p2 < len(nums2) and nums1[p1] < nums2[p2]:
                        p1 += 1
                    while p2 < len(nums2) and p1 < len(nums1) and nums2[p2] < nums1[p1]:
                        p2 += 1
                    if p1 < len(nums1) and p2 < len(nums2) and nums1[p1] == nums2[p2]:
                        res.append(nums2[p2])
                        p2 += 1
                        p1 += 1
                return res