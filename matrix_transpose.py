# matrix = [[1, 2, 3],[4, 5, 6]]
# matrix = [[1, 2, 3]]
# matrix = [[7, 8], [9, 10], [11, 12]]
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
for i in range(len(matrix[0])):
    row_entries = []
    for j in range(len(matrix)):
        data = matrix[j][i]
        row_entries.append(data)
    new_matrix.append(row_entries)

print(f"transpose of matrix: {new_matrix}")
