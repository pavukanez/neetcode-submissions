class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        self.seen = set()

        def dfs(r, c, d):
            # Only block out-of-bounds, walls (-1), or already visited cells in this path
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in self.seen:
                return
            
            # If the current distance is greater than or equal to what's already there, stop exploring deeper
            if grid[r][c] < d:
                return

            self.seen.add((r, c))
            grid[r][c] = min(grid[r][c], d)

            dfs(r - 1, c, d + 1)
            dfs(r + 1, c, d + 1)
            dfs(r, c + 1, d + 1)
            dfs(r, c - 1, d + 1)
            
            self.seen.remove((r, c)) # Clean up backtracking for other paths if needed

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
                    self.seen = set()