# Problem: Count even and odd numbers
arr = [1, 2, 3, 4, 5, 6]
even = odd = 0

for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
