class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            if 0 < min_index < len(arr) - 1:
                res += min(arr[min_index - 1], arr[min_index + 1]) * arr[min_index]
            else:
                res += arr[1 if min_index == 0 else min_index - 1] * arr[min_index]
            arr.pop(min_index)
        return res
