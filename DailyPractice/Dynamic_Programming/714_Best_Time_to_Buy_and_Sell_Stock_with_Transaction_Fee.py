class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy, sell = float('-inf'), 0
        for p in prices:
            buy, sell = max(sell - p, buy), max(sell, buy + p - fee)
        return sell