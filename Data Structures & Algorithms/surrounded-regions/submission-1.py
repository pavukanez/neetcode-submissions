class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def mark_safe(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] == "X" or board[r][c] == "T":
                return
            board[r][c] = "T"

            mark_safe(r - 1, c)
            mark_safe(r + 1, c)
            mark_safe(r, c - 1)
            mark_safe(r, c + 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                mark_safe(r, 0)
            if board[r][COLS - 1] == "O":
                mark_safe(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                mark_safe(0, c)
            if board[ROWS - 1][c] == "O":
                mark_safe(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

            