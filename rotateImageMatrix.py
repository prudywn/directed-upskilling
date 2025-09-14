class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #Swap diagonals by leading diagonal
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #Reverse row
        for i in range(n):
            matrix[i].reverse()