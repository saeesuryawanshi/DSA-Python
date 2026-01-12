# Check if an array is already sorted

def is_sorted(arr):
    """
    Returns True if the array is sorted in non-decreasing order
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Test the function
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    
    if is_sorted(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")

# Time Complexity: O(n)
# Space Complexity: O(1)
