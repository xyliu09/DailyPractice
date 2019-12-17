class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        area = 0
        while left < right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                area += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                area += maxRight - height[right]
                right -= 1
        return area
