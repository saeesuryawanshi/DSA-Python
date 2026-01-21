# Find Second Largest Element in an Array
# Using built-in and without built-in functions

def second_largest_builtin(arr):
    if len(arr) < 2:
        return "Length of array must be at least 2."

    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return "No second largest element (all elements same)"

    unique_arr.sort()
    return unique_arr[-2]


def second_largest_manual(arr):
    if len(arr) < 2:
        return "Length of array must be at least 2."

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element (all elements same)"

    return second_largest

arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("Second largest (using built-in):", second_largest_builtin(arr))
print("Second largest (without built-in):", second_largest_manual(arr))
