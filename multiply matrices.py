import time
import random

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must be equal to number of rows in matrix2")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def calculate_time_complexity(rows, cols):
    matrix1 = generate_random_matrix(rows, cols)
    matrix2 = generate_random_matrix(cols, rows)
    
    start_time = time.time()
    result = multiply_matrices(matrix1, matrix2)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Time Complexity: O({})".format(rows * cols * (cols + 1)))  # O(n^3) for matrix multiplication
    print("Elapsed Time: {:.6f} seconds".format(elapsed_time))

# Example usage:
calculate_time_complexity(100, 100)
