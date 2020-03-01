'''
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return 1
    else:
        return 0


def exponentialGrowth(arr, n):
    arr.sort()
    if n > arr[-1] or n < arr[0]:
        return n
    while n <= arr[-1] and BinarySearch(arr, n):
        n *= 2
    return n

'''

from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def exponentialGrowth(arr, n):
    arr.sort()
    if n > arr[-1] or n < arr[0]:
        return n

    for i in arr:
        if i == n:
            n *= 2

    return n