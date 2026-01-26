# Count vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
