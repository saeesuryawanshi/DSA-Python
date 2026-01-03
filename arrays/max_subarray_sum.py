# Problem: Maximum subarray sum (Kadane's Algorithm)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = maximum = arr[0]
for x in arr[1:]:
    current = max(x, current + x)
    maximum = max(maximum, current)

print(maximum)
