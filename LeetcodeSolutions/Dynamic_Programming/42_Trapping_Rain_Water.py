class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        maxleft, maxright = [height[0] for _ in height], [height[-1] for _ in height]
        for i in range(1, len(height)):
            maxleft[i] = max(maxleft[i - 1], height[i])
        for j in range(len(height) - 2, -1, -1):
            maxright[j] = max(maxright[j + 1], height[j])
        for i in range(1, len(height) - 1):
            area += max(0, min(maxleft[i], maxright[i]) - height[i])

        return area
