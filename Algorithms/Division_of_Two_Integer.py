class Solution(object):
    def divisor(self, a, b):
        if b == 0:
            return 'NaN'
        ans = []
        seen = set()
        dotHasPut = False
        while True:
            if a in seen:
                ans[-1] = '(' + ans[-1] + ')'
                break
            num, div = a // b, (a % b)
            ans.append(str(num))
            if not dotHasPut:
                ans.append('.')
                dotHasPut = True
            if div == 0:
                break
            seen.add(a)
            a = div * 10
        return ''.join(ans)


def main():
    obj = Solution()
    for x, y in [(1, 2), (1, 3)]:
        test = obj.divisor(x, y)
        print(test, x, y)


if __name__ == "__main__":
    main()
