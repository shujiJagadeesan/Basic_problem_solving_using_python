def is_palindrome(number):
    given_number = number
    reverse_of_number = 0
    while given_number != 0:
        digit = given_number % 10
        reverse_of_number = reverse_of_number * 10 + digit
        given_number //= 10
    if (reverse_of_number == number):
        return True
    else:
        return False
number = int(input("Enter a number to determine whether it is a palindrome or not: "))
palindrome_result = is_palindrome(number)
if palindrome_result:
    print("Yes, the number is a palindrome")
else:
    print("No, the number is not a palindrome")