class Solution {
    private int rows, cols;
    int[][] seen;

    public int islandPerimeter(int[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        seen = new int[rows][cols];

        for(int r=0;r<rows;r++){
            for(int c=0;c<cols;c++){
                if (grid[r][c] == 1){
                    return dfs(grid, r, c);
                }
            }
        }

        return -1;
        
    }

    public int dfs(int[][] grid, int r, int c){
        if (r < 0 || r == rows || c < 0 || c == cols || grid[r][c] == 0){
            return 1;
        }

        if (seen[r][c] == 1){
            return 0;
        }

        seen[r][c] = 1;

        return dfs(grid, r - 1, c) + dfs(grid, r + 1, c) + dfs(grid, r, c - 1) + dfs(grid, r, c + 1);
    }
}