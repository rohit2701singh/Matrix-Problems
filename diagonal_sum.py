shape_input = int(input("row in square matrix: "))

matrix_list = []
for _ in range(shape_input):
    num_str_row = input("input numbers separated by space: ").strip()
    num_int_row = list(map(int, num_str_row.split()))
    matrix_list.append(num_int_row)
print(matrix_list)

left_to_right_sum = 0
for i in range(shape_input):
    left_to_right_sum += matrix_list[i][i]
print("LR diagonal sum:", left_to_right_sum)

right_to_left_sum = 0
for i in range(shape_input):
    right_to_left_sum += matrix_list[i][shape_input-1-i]
print("RL diagonal sum:", right_to_left_sum)

difference_of_sum = abs(left_to_right_sum - right_to_left_sum)
print("absolute difference of sum is:", difference_of_sum)