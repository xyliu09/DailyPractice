class Solution:
    def shipWithinDays(self, weights, D):
        l, r = min(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if self.f(weights, mid) < D:
                r = mid - 1
            else:
                l = mid + 1
        return min(l, r)

    def f(self, weights, mid):
        sum_, count = 0, 0
        for i in range(len(weights)):
            sum_ += weights[i]

            if sum_ > mid:
                count += 1
                sum_ = weights[i]
            if len(weights) == i + 1:
                count += 1

        return count
