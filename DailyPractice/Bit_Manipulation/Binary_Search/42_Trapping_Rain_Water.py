class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max, right_max = [height[0]] * len(height) , [height[-1]] * len(height)
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(len(height)-2, 0, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans