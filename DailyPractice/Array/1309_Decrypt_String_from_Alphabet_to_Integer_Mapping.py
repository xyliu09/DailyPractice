from string import ascii_lowercase
class Solution:
    def freqAlphabets(self, s: str) -> str:
        table = {}
        for n, c in enumerate(ascii_lowercase):
            if n + 1 >= 10:
                table[c] = str(n+1)+'#'
            else:
                table[c] = str(n+1)
        for k, v in list(table.items())[::-1]:
            s = s.replace(v, k)
        return s