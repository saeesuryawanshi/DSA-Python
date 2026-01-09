#Reverse string wihtout using readymade function
string = input("Enter the string: ")

rev_str=""
for ch in string:
    rev_str = ch + rev_str
print(rev_str)
