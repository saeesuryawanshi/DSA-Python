# Check whether two strings are anagrams
# Two strings are anagrams if they contain the same characters
# with the same frequency (order does not matter)

def anagram_check(str1, str2):
    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}

    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2


# User input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if anagram_check(str1, str2):
    print("Anagram")
else:
    print("Not Anagram")


# Time Complexity: O(n)
# Space Complexity: O(n)
