#Reverse the array
arr = [1, 2, 3, 4, 5]

print("usinf built in funtion:")
print(arr[::-1])

def reverse_arr(arr):
    i=len(arr)-1
    while i>=0:
        print(arr[i],end=" ")
        i-=1
      
print("without using function")
reverse_arr(arr)

# Time Complexity:
# Both approaches -> O(n)

# Space Complexity:
# Built-in slicing -> O(n)
# Without built-in -> O(1)
