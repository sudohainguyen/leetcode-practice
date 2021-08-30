class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        #swap along diagonal
        for i in range(0,row):
            for j in range(i,col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #flip horizontally
        for i in range(row):
            for j in range(col//2):
                matrix[i][j], matrix[i][row-1-j] = matrix[i][row-1-j],matrix[i][j]
        