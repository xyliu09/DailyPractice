'''

Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.

Output:

Print the minimum number of characters.

Constraints:

1 ≤ T ≤ 50
1 ≤ S ≤ 40

Example:

Input:
3
abcd
aba
geeks

Output:
3
0
3



** For More Input/Output Examples Use 'Expected Output' option **
'''

import sys


# Recursive function to find minimum
# number of insertions
def findMinInsertions(str, l, h):
    # Base Cases
    if (l > h):
        return sys.maxsize
    if (l == h):
        return 0
    if (l == h - 1):
        return 0 if (str[l] == str[h]) else 1

    # Check if the first and last characters are
    # same. On the basis of the comparison result,
    # decide which subrpoblem(s) to call

    if (str[l] == str[h]):
        return findMinInsertions(str, l + 1, h - 1)
    else:
        return (min(findMinInsertions(str, l, h - 1),
                    findMinInsertions(str, l + 1, h)) + 1) 