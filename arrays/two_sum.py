# Problem: Find indices of two numbers that add up to target
arr = [2, 7, 11, 15]
target = 9

seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        print(seen[target - num], i)
        break
    seen[num] = i
