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
                first_matrix.append(row_items.split(' '))
                # first_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\n**This row will not go in matrix. Please enter row data again. Do not put unnecessary space\n")
    while True:
        row_items = input("MATRIX-2; enter row numbers separated with space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            print(f"shape of second matrix(row, column): {(len(second_matrix), len(second_matrix[0]))}")
            break
        else:
            try:
                second_matrix.append(row_items.split(' '))
                # second_matrix.append(list(map(int, row_items.split(' '))))
            except ValueError:
                print("\nThis row will not go in matrix. Please enter row data again. Do not put space at the end\n")
    is_finished = True

print(f"\nmatrix 1: {first_matrix} & matrix 2: {second_matrix}")