class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def is_not_underattack(r, c):
            return not (cols[c] or hill_diagnals[r - c] or dale_diagnals[r + c])

        def place_queen(r, c):
            cols[c] = 1
            hill_diagnals[r - c] = 1
            dale_diagnals[r + c] = 1

        def remove_queen(r, c):
            cols[c] = 0
            hill_diagnals[r - c] = 0
            dale_diagnals[r + c] = 0

        def backtrack(row=0, count=0):
            for col in range(n):
                if is_not_underattack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        cols = [0] * n
        hill_diagnals = [0] * (2 * n - 1)
        dale_diagnals = [0] * (2 * n - 1)
        return backtrack()


