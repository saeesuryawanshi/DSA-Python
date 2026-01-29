# Check if a string is a palindrome without using built-in reverse

def is_palindrome_manual(s):
    s = s.replace(" ", "").lower()
    n = len(s)
    
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

s = input("Enter a string: ")

if is_palindrome_manual(s):
    print(f'"{s}" is a palindrome')
else:
    print(f'"{s}" is not a palindrome')
