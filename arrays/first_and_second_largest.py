# Find First and Second Largest Elements in an Array
# Without using sorting or built-in functions

def first_and_second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num != first and num > second:
            second = num

    if second == float('-inf'):
        return "No second largest element"

    return first, second


# User input
arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = first_and_second_largest(arr)

print("Result:", result)

# Time Complexity: O(n)
# Space Complexity: O(1)
