class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(r, c):
            return not (cols[c] + hill_diagnals[r - c] + dale_diagnals[r + c])

        def place_queen(r, c):
            queens.add((r, c))
            cols[c] = 1
            hill_diagnals[r - c] = 1
            dale_diagnals[r + c] = 1

        def add_solution():
            solutions = []
            for _, col in sorted(queens):
                solutions.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solutions)

        def remove_queen(r, c):
            queens.remove((r, c))
            cols[c] = 0
            hill_diagnals[r - c] = 0
            dale_diagnals[r + c] = 0

        def backtrack(row=0):
            for col in range(n):
                if can_place(row, col):

                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagnals = [0] * (2 * n - 1)
        dale_diagnals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output


