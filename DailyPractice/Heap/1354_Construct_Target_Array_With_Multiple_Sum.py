'''
Share
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

'''
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        q = [-x for x in target]
        heapq.heapify(q)
        while -q[0] * 2 > s:
            n = -heapq.heappop(q)
            heapq.heappush(q, -2 * n + s)
            s = n
        return s == len(target)