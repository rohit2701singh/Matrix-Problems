first_matrix = []
second_matrix = []

is_finished = False
while not is_finished:

    while True:
        row_items = input("MATRIX-1; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"total row in first matrix: {len(first_matrix)}")
            break
        else:
            try:
                first_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\n**This row will not go in matrix. Please enter row data again. Do not put unnecessary space\n")
    while True:
        row_items = input("MATRIX-2; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"total row in second matrix: {len(first_matrix)}")
            break
        else:
            try:
                second_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\nThis row will not go in matrix. Please enter row data again. Do not put space at the end\n")
    is_finished = True

print(f"matrix 1: {first_matrix} & matrix 2: {second_matrix}")

new_matrix = []
for list_num in range(len(first_matrix)):
    matrix_row_data = []
    for i in range(len(first_matrix[list_num])):
        matrix_sum = first_matrix[list_num][i] + second_matrix[list_num][i]
        matrix_row_data.append(matrix_sum)

    new_matrix.append(matrix_row_data)

print(f"sum of two matrix: {new_matrix}")