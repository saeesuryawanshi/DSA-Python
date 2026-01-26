# Character Frequency in a String
# Counts how many times each character appears

def char_frequency(s):
    freq = {}

    for ch in s:
        if ch == " ":
            continue   # ignore spaces
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq


# User input
s = input("Enter a string: ")
result = char_frequency(s)

print("Character Frequency:")
for key, value in result.items():
    print(f"{key} : {value}")

# Time Complexity: O(n)
# Space Complexity: O(n)
