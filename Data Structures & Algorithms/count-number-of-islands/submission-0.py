class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                self.dfs(i, j, grid)
                count += 1
        return count

    def dfs(self, i, j, grid):
        if i > -1 and i < len(grid) and j > -1 and j < len(grid[0]) and grid[i][j] == "-1":
            grid[i][j] = "0"
            dfs(grid[i-1][j])
            dfs(grid[i+1][j])
            dfs(grid[i][j-1])
            dfs(grid[i][j+1])


        
