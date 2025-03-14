def check_string_palindrome(str):
    i = 0
    j = len(str)-1
    is_palindrome = True
    while i < j:
        if str[i] != str[j]:
            is_palindrome = False
            break
        i+=1
        j-=1
    return True if is_palindrome else False
str = input("Enter a string to check if it is a palindrome or not: ")
if(check_string_palindrome(str)):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")

