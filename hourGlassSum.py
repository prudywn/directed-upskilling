class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass_sums = []
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows-2):
            for j in range(cols-2):
                top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                middle = grid[i+1][j+1]
                bottom = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                sums = top + middle + bottom

                hourglass_sums.append(sums)
                result = max(hourglass_sums)
        
        return result
        