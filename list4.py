
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


sums = [sum(inner_list) for inner_list in nested_list]


print("Nested List:", nested_list)
print("Sum of each inner list:", sums)
