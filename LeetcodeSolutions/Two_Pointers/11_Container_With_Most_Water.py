class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p, q = 0, len(height) - 1
        maxArea = 0
        while p < q:
            maxArea = max(maxArea, min(height[p], height[q]) * (q - p))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return maxArea
