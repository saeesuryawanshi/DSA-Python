# Linear Search Algorithm
# Works on both sorted and unsorted arrays

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# User input
arr = list(map(int, input("Enter elements separated by space: ").split()))
target = int(input("Enter element to search: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Time Complexity: O(n)
# Space Complexity: O(1)
