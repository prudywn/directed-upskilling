class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [(0) * n for _ in range(m)]

        #Mark walls and Guards
        for r, c in guards:
            grid[r][c] = 'G'

        for r, c in walls:
            grid[r][c] = 'W'

        #Directions up,down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        ##Spread vision
        for r, c in guards:
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in ("G", "W"):   # blocked
                        break
                    if grid[nr][nc] == 0:            # mark as guarded
                        grid[nr][nc] = "X"
                    nr += dr
                    nc += dc
        
         # Count unguarded (still 0)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count