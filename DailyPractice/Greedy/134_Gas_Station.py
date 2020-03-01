class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank, start, total, = 0, 0, 0
        for i, ga in enumerate(gas):
            tank += ga - cost[i]
            if tank < 0:
                start, total, tank = i + 1, tank + total, 0

        return -1 if total + tank < 0 else start