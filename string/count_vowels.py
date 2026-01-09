# Program to count vowels in a string (including uppercase)

# Input from user
string = input("Enter the string to count vowels: ")

# List of vowels (both lowercase and uppercase)
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Initialize count
count = 0

# Traverse through each character in the string
for ch in string:
    if ch in vowels:
        count += 1

# Print the result
print(f"Number of vowels: {count}")
