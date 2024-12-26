import numpy as np

def get_matrix_input():
    """Gets matrix input from the user."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element at row {i+1}, column {j+1}: ")))
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix):
    """Prints the matrix in a formatted way."""
    for row in matrix:
        print(row)

while True:
    print("\nMatrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Calculate Determinant")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter the first matrix:")
        matrix1 = get_matrix_input()
        print("Enter the second matrix:")
        matrix2 = get_matrix_input()
        if matrix1.shape == matrix2.shape:
            result = np.add(matrix1, matrix2)
            print("Result:")
            print_matrix(result)
        else:
            print("Matrices must have the same dimensions for addition.")

    elif choice == 2:
        print("Enter the first matrix:")
        matrix1 = get_matrix_input()
        print("Enter the second matrix:")
        matrix2 = get_matrix_input()
        if matrix1.shape == matrix2.shape:
            result = np.subtract(matrix1, matrix2)
            print("Result:")
            print_matrix(result)
        else:
            print("Matrices must have the same dimensions for subtraction.")

    elif choice == 3:
        print("Enter the first matrix:")
        matrix1 = get_matrix_input()
        print("Enter the second matrix:")
        matrix2 = get_matrix_input()
        if matrix1.shape[1] == matrix2.shape[0]:
            result = np.dot(matrix1, matrix2)
            print("Result:")
            print_matrix(result)
        else:
            print("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")

    elif choice == 4:
        print("Enter the matrix:")
        matrix = get_matrix_input()
        result = np.transpose(matrix)
        print("Transpose:")
        print_matrix(result)

    elif choice == 5:
        print("Enter the matrix:")
        matrix = get_matrix_input()
        if matrix.shape[0] == matrix.shape[1]:
            result = np.linalg.det(matrix)
            print("Determinant:", result)
        else:
            print("Determinant can only be calculated for square matrices.")

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please try again.")