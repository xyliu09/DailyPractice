class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, i, area = [], 0, 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                area += distance * h
            stack.append(i)
            i += 1
        return area
