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
                matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\n**This row will not go in matrix. Please enter row data again. Do not put unnecessary space\n")
    is_finished = True

new_matrix = []
for arr in matrix:
    for item in arr:
        new_matrix.append(item)
print(new_matrix)