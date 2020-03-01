class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            switch = {1: 'One',
                      2: 'Two',
                      3: 'Three',
                      4: 'Four',
                      5: 'Five',
                      6: 'Six',
                      7: 'Seven',
                      8: 'Eight',
                      9: 'Nine',
                      }
            return switch[num]

        def two_less_20(num):
            switch = {10: 'Ten',
                      11: 'Eleven',
                      12: 'Twelve',
                      13: 'Thirteen',
                      14: 'Fourteen',
                      15: 'Fifteen',
                      16: 'Sixteen',
                      17: 'Seventeen',
                      18: 'Eighteen',
                      19: 'Nineteen'}
            return switch[num]

        def ten(num):
            switch = {20: 'Twenty',
                      30: 'Thirty',
                      40: 'Forty',
                      50: 'Fifty',
                      60: 'Sixty',
                      70: 'Seventy',
                      80: 'Eighty',
                      90: 'Ninety'}
            return switch[num]

        def two(num):
            res = ''
            if not num:
                return res
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            res += ten((num // 10) * 10)
            num %= 10
            if num:
                res += ' ' + one(num)
            return res

        def three(num):
            if num < 100:
                return two(num)
            res = one(num // 100) + ' Hundred'
            num %= 100
            res += ' ' if num else ''
            return res + two(num)

        if not num:
            return 'Zero'
        res = ''
        billion = num // 1000000000
        if billion:
            res += ' ' if res else ''
            res += three(billion) + ' Billion'
        num %= 1000000000
        million = num // 1000000
        if million:
            res += ' ' if res else ''
            res += three(million) + ' Million'
        num %= 1000000
        thousand = num // 1000
        if thousand:
            res += ' ' if res else ''
            res += three(thousand) + ' Thousand'
        num %= 1000
        res += ' ' if num and res else ''
        return res + three(num)