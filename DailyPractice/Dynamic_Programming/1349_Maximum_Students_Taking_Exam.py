import functools


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        m = len(seats)
        n = len(seats[0])
        validity = []

        def countBit(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        for i in range(m):
            curr = 0
            for j in range(n):
                curr = (curr << 1) + (seats[i][j] == ".")
            validity.append(curr)

        dp = [[-1 for _ in range(1 << n)] for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):

            valid = validity[i - 1]
            for j in range(1 << n):
                if (j & valid) == j and not (j & (j >> 1)):
                    for k in range(1 << n):
                        if dp[i - 1][k] != -1 and not (j & (k << 1)) and not (j & (k >> 1)):
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + countBit(j))
        return max(dp[-1])