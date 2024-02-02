def get_matrix():
    list_item = []
    while True:
        row_items = input("Enter row numbers separated by space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            return list_item
        else:
            try:
                list_item.append(row_items.split())
                # matrix.append(list(map(int, row_items.split())))
            except ValueError:
                print("Invalid input. Please enter row data again.")


matrix = get_matrix()
print(f"Shape of first matrix (row, column): {(len(matrix), len(matrix[0]))}")
print(f"matrix: {matrix}")

new_matrix = []
for arr in matrix:
    for item in arr:
        new_matrix.append(item)
print(f"final 1D list from matrix: {new_matrix}")
