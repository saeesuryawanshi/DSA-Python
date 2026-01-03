# Problem: Move all zeros to end of array
arr = [0, 1, 0, 3, 12]

non_zero = [x for x in arr if x != 0]
zeros = [0] * (len(arr) - len(non_zero))
print(non_zero + zeros)
