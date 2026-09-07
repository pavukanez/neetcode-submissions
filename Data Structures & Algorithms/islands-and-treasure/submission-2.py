class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        self.seen = set()

        def dfs(r, c, d):
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or grid[r][c] == -1 or (r, c) in self.seen:
                return
            self.seen.add((r, c))

            if grid[r][c] < d:
                return
            grid[r][c] = min(grid[r][c], d)

            dfs(r - 1, c, d + 1)
            dfs(r + 1, c, d + 1)
            dfs(r, c + 1, d + 1)
            dfs(r, c - 1, d + 1)

            self.seen.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
                    self.seen = set()
