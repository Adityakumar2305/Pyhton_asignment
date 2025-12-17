
import copy

original = [[1, 2], [3, 4]]

## Shallow copy
shallow = original.copy()

# Deep copy
deep = copy.deepcopy(original)

# Modify original
original[0][0] = 99

print("Original:", original)
print("Shallow copy:", shallow)
