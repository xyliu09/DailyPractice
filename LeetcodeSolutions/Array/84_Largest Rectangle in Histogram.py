class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i in range(len(heights)+1):
            h = 0 if i == len(heights) else heights[i]
            while stack and h < heights[stack[-1]]:
                currheight = heights[stack.pop()]
                previndex = -1 if not stack else stack[-1]
                res = max(res, (i - previndex - 1) * currheight)
            stack.append(i)
        return res