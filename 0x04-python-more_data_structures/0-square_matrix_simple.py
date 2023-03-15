#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def square_matrix_simple(matrix=[]):
    # Get the dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Create a new matrix with the same dimensions as the input matrix
    result = [[0] * cols for _ in range(rows)]
    
    # Fill in the values of the new matrix as squares of the input values
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] ** 2
            
    return result

