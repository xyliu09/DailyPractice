class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        ans = []
        for x,y in queries:
            if x == 0:
                ans.append(arr[y])
            else:
                ans.append(arr[x-1]^arr[y])
        return ans