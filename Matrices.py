# A matrix in Python can be represented as a nested list, where each sub-list represents a row of the matrix.

# Define a 2x2 matrix
matrix1 = [[1, 2],
           [3, 4]]

# We can access an element of the matrix by specifying its row and column indices.
print("The element at row 1 and column 0 is: ", matrix1[1][0])  # Outputs: 3

# We can also modify an element of the matrix.
matrix1[1][0] = 5
print("The modified matrix is: ", matrix1)  # Outputs: [[1, 2], [5, 4]]


# Another 2x2 matrix
matrix2 = [[5, 6],
           [7, 8]]

# We can add two matrices element-wise
result = [[0, 0],
          [0, 0]]  # Initialise a matrix to hold the result

for i in range(len(matrix1)):  # Iterate over rows
    for j in range(len(matrix1[0])):  # Iterate over columns
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("The sum of the two matrices is: ", result)  # Outputs: [[6, 8], [12, 12]]

# Note: Python has several libraries such as NumPy that can handle matrices more efficiently and provide more operations

