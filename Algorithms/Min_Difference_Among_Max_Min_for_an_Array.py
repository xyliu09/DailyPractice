import sys

def minDifferenceAmongMaxMin(arr, N, k):
    arr.sort()
    ans = sys.maxsize
    for i in range(N-K+1):
        currmin = arr[i+K-1] - arr[i]
        ans = min(ans, currmin)
    return ans


arr = [10, 20, 30, 100, 101, 102]
N = len(arr)
K = 3
print(minDifferenceAmongMaxMin(arr, N, K)) 