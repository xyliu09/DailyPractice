class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, minPrice = 0, float('inf')
        for p in prices:
            maxProfit, minPrice = max(maxProfit, p - minPrice), min(minPrice, p)
        return maxProfit