# matrix = [[1, 2, 3],[4, 5, 6]]
# matrix = [[1, 2, 3]]
# matrix = [[7, 8], [9, 10], [11, 12]]
matrix = []

is_finished = False
while not is_finished:

    while True:
        row_items = input("MATRIX-1; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"shape of first matrix(row, column): {(len(matrix), len(matrix[0]))}")
            break
        else:
            try:
                matrix.append(row_items.split(' '))
                # matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\n**This row will not go in matrix. Please enter row data again. Do not put unnecessary space\n")
    is_finished = True

new_matrix = []
for i in range(len(matrix[0])):
    row_entries = []
    for j in range(len(matrix)):
        data = matrix[j][i]
        row_entries.append(data)
    new_matrix.append(row_entries)
print(new_matrix)
