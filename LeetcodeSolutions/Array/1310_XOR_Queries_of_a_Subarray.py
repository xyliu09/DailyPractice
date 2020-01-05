class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xarray = [arr[0] for _ in arr]
        for i in range(1, len(arr)):
            xarray[i] = xarray[i-1]^arr[i]
        ans = []
        for L, R in queries:
            if L == 0:
                ans.append(xarray[R])
            else:
                ans.append(xarray[R]^xarray[L-1])
        return ans