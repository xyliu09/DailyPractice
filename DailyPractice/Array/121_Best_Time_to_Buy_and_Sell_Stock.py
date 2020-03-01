class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice, maxProfit = float('inf'), 0
        for p in prices:
            maxProfit = max(p - minPrice, maxProfit)
            minPrice = min(p, minPrice)
        return maxProfit