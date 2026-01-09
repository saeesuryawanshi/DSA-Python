# sum_of_list.py
# Sum of all elements in a list (Python)
# This program calculates the sum of all elements in a list using Python

def sum_of_list(lst):
    """
    Returns the sum of all elements in the list lst
    """
    total = 0
    for num in lst:
        total += num
    return total

# Test the function with user input
if __name__ == "__main__":
    # Take input from the user
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    
    print("List:", arr)
    print("Sum of all elements:", sum_of_list(arr))

# Time Complexity: O(n), n = number of elements in the list
# Space Complexity: O(1), only one variable used
