# Bubble Sort in Python
# Repeatedly compares adjacent elements and swaps them if they are in wrong order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swap happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap, array is already sorted
        if not swapped:
            break

# Test the function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    bubble_sort(arr)

    print("Sorted array:", arr)

# Time Complexity:
# Best Case: O(n)  (already sorted)
# Average Case: O(n^2)
# Worst Case: O(n^2)

# Space Complexity:
# O(1) (in-place sorting)
