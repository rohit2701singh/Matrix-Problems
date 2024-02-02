def get_matrix():
    matrix = []
    while True:
        row_items = input("Enter row numbers separated by space (type 'end' when matrix complete): ").lower()
        if row_items == 'end':
            return matrix
        else:
            try:
                matrix.append(row_items.split())
                # matrix.append(list(map(int, row_items.split())))
            except ValueError:
                print("Invalid input. Please enter row data again.")


first_matrix = get_matrix()
print(f"Shape of first matrix (row, column): {(len(first_matrix), len(first_matrix[0]))}")

second_matrix = get_matrix()
print(f"Shape of second matrix (row, column): {(len(second_matrix), len(second_matrix[0]))}")

print(f"first matrix: {first_matrix}\nsecond matrix: {second_matrix}")
