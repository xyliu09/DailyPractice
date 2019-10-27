class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i - c] + 1, dp[i])

        return dp[amount] if dp[amount] != amount + 1 else -1