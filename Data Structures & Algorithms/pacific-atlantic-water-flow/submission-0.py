class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)

        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res 