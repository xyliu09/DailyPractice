class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1: return 0
        memo = [0 for _ in range(amount)]
        return self.helper(coins, amount, memo)

    def helper(self, coins, amount, memo):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if memo[amount - 1] != 0:
            return memo[amount - 1]
        minVal = 2 ** 31
        for c in coins:
            res = self.helper(coins, amount - c, memo)
            if res >= 0 and res < minVal:
                minVal = 1 + res
        memo[amount - 1] = -1 if minVal == 2 ** 31 else minVal
        return memo[amount - 1]