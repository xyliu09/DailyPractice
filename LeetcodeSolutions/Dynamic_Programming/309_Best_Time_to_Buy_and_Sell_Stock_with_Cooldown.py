class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, buy_minus1, sell_minus1, sell_minus2 = float('-inf'), 0, float('-inf'), 0, 0
        for p in prices:
            buy_minus1, sell_minus2, sell_minus1 = buy, sell_minus1, sell
            buy, sell = max(buy_minus1, sell_minus2 - p), max(buy_minus1 + p, sell_minus1)
        return sell