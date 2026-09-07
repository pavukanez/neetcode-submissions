class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])

        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= self.ROWS or c < 0 or c >= self.COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count