class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solns = []

        # rows currently occupied
        rows = set()

        # main diagonal (r - c)
        diag1 = set()

        # anti-diagonal (r + c)
        diag2 = set()

        curr_res = []      # (row, col) of queens

        def backtrack(col):
            # Found a complete placement
            if col == n:
                board = [["."] * n for _ in range(n)]

                for r, c in curr_res:
                    board[r][c] = "Q"

                solns.append(["".join(row) for row in board])
                return

            for row in range(n):

                # Cannot place here
                if row in rows:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Place queen
                rows.add(row)
                diag1.add(row - col)
                diag2.add(row + col)
                curr_res.append((row, col))

                backtrack(col + 1)

                # Remove queen
                curr_res.pop()
                rows.remove(row)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return solns