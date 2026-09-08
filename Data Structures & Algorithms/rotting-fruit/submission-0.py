class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        res = 0

        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        queue.append((row, col))

            res += 1
        return res if fresh == 0 else -1
                



