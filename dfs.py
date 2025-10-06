class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # m x n
        # left, top Pacific
        # right, bottom Atlantic

        # DFS

        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_h):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited
                or heights[r][c] < prev_h
                ):
                return
            
            visited.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # DFS from Pacifc (top and left) and Atlantic
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Intersection
        return list(pacific & atlantic)