class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        res, rows, cols = 0, len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)

                    def dfs(r, c):
                        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                            return
                        grid[r][c] = 0
                        area += 1
                        dfs(r - 1, c)
                        dfs(r + 1, c)
                        dfs(r, c - 1)
                        dfs(r, c + 1)
                    res = max(res, area)
        return res


