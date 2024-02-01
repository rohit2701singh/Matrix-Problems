first_matrix = []
second_matrix = []

is_finished = False
while not is_finished:

    while True:
        row_items = input("MATRIX-1; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"shape of first matrix(row, column): {(len(first_matrix), len(first_matrix[0]))}")
            break
        else:
            try:
                first_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\n**This row will not go in matrix. Please enter row data again. Do not put unnecessary space\n")
    while True:
        row_items = input("MATRIX-2; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"shape of second matrix(row, column): {(len(second_matrix), len(second_matrix[0]))}")
            break
        else:
            try:
                second_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\nThis row will not go in matrix. Please enter row data again. Do not put space at the end\n")
    is_finished = True

# first_matrix = [[1], [2], [3]]  # test example pair
# second_matrix = [[1, 2, 3]]

# first_matrix = [[3, 2], [1, 4], [5, 3]]     # test example pair
# second_matrix = [[3, 2], [1, 4]]

# first_matrix = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]     # test example pair
# second_matrix = [[4, 5, 6], [9, 6, 3], [7, 8, 9]]

print(f"\nmatrix 1: {first_matrix} & matrix 2: {second_matrix}")

first_matrix_rows = len(first_matrix)
first_matrix_columns = len(first_matrix[0])
second_matrix_rows = len(second_matrix)
second_matrix_columns = len(second_matrix[0])

if first_matrix_columns == second_matrix_rows:
    print(f"matrix multiplication is possible and new matrix's shape will be (rows, column): "
          f"{(first_matrix_rows, second_matrix_columns)}")

    new_matrix = []
    for i in range(len(first_matrix)):      # total rows
        row_list = []
        for j in range(len(second_matrix[0])):   # element in a row in second list
            data_sum = 0
            for k in range(len(first_matrix[0])):   # element in single list
                row_data = first_matrix[i][k] * second_matrix[k][j]
                data_sum += row_data
            row_list.append(data_sum)
        print(row_list)
        new_matrix.append(row_list)
    print(f"here is final matrix: {new_matrix}")

else:
    print("matrix multiplication not possible")

# analyse this and then code:
# first_row = [[
#         first_matrix[0][0] * second_matrix[0][0] +
#         first_matrix[0][1] * second_matrix[1][0] +
#         first_matrix[0][2] * second_matrix[2][0],

#         first_matrix[0][0] * second_matrix[0][1] +
#         first_matrix[0][1] * second_matrix[1][1] +
#         first_matrix[0][2] * second_matrix[2][1],

#         first_matrix[0][0] * second_matrix[0][2] +
#         first_matrix[0][1] * second_matrix[1][2] +
#         first_matrix[0][2] * second_matrix[2][2]
#     ] ]
