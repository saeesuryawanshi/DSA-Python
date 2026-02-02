# Binary Search Algorithm
# Works only on SORTED arrays

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# User input
arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter element to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Time Complexity: O(log n)
# Space Complexity: O(1)
