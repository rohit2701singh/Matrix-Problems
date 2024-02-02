def get_matrix():
    matrix = []
    while True:
        row_items = input("Enter row numbers separated by space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            return matrix
        else:
            try:
                # matrix.append(row_items.split())
                matrix.append(list(map(int, row_items.split())))
            except ValueError:
                print("Invalid input. Please enter row data again.")


first_matrix = get_matrix()
second_matrix = get_matrix()

print(f"matrix 1: {first_matrix} & matrix 2: {second_matrix}")
print(f"Shape of first matrix (row, column): {(len(first_matrix), len(first_matrix[0]))}")
print(f"Shape of second matrix (row, column): {(len(second_matrix), len(second_matrix[0]))}")


if len(first_matrix) == len(second_matrix) and len(first_matrix[0]) == len(second_matrix[0]):
    new_matrix = []
    for list_num in range(len(first_matrix)):
        matrix_row_data = []
        for i in range(len(first_matrix[list_num])):
            matrix_sum = first_matrix[list_num][i] + second_matrix[list_num][i]
            matrix_row_data.append(matrix_sum)

        new_matrix.append(matrix_row_data)

    print(f"sum of two matrix: {new_matrix}")
else:
    print("sum is not possible")
